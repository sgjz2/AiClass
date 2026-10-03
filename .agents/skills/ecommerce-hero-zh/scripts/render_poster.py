"""Reusable ordered-layer poster renderer. Python 3 + Pillow; no image API calls."""
import argparse
import hashlib
import json
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps


def checked_box(value,canvas_size):
    x,y,w,h=map(int,value)
    if min(x,y)<0 or min(w,h)<=0 or x+w>canvas_size[0] or y+h>canvas_size[1]:
        raise ValueError(f'Box outside canvas: {value}')
    return x,y,w,h


def typeset(value,face,size,tracking,gap):
    """Build text on a transparent layer, then measure the rendered glyphs."""
    f=ImageFont.truetype(str(face),size)
    lines=value.split('\n')
    widths=[f.getlength(s)+tracking*max(0,len(s)-1) for s in lines]
    if min(widths)<0 or size+gap<=0:
        raise ValueError('Invalid tracking or line spacing')
    pad=size*2
    layer=Image.new('RGBA',(max(1,math.ceil(max(widths)))+pad*2,
                            (size+gap)*len(lines)+pad*2))
    d=ImageDraw.Draw(layer)
    for row,line in enumerate(lines):
        baseline=pad+size+row*(size+gap)
        if tracking==0:
            d.text((pad,baseline),line,font=f,fill='white',anchor='ls')
        else:
            for index,char in enumerate(line):
                advance=f.getlength(line[:index])+index*tracking
                d.text((pad+advance,baseline),char,font=f,fill='white',anchor='ls')
    bounds=layer.getchannel('A').getbbox()
    if bounds is None:
        raise ValueError('Empty text layer')
    return layer.crop(bounds)


def render(config_path,output_path,font_dir=None):
    config_path=Path(config_path).resolve()
    data=json.loads(config_path.read_text(encoding='utf-8-sig'))
    root=config_path.parent
    resolve=lambda p: Path(p) if Path(p).is_absolute() else root/p
    size=tuple(map(int,data['size']))
    if len(size)!=2 or min(size)<=0:
        raise ValueError('Positive width/height required')
    canvas=Image.new('RGBA',size,data.get('canvas_fill','#F5F3EE'))
    if data.get('background'):
        bg=Image.open(resolve(data['background'])).convert('RGBA')
        box=checked_box(data.get('background_box',[0,0,*size]),size)
        if 'background_box' not in data and abs(bg.width/bg.height/(size[0]/size[1])-1)>.02:
            raise ValueError('Declare background_box for an intentional aspect-ratio crop')
        center=tuple(data.get('crop_position',[.5,.5]))
        if len(center)!=2 or any(v<0 or v>1 for v in center):
            raise ValueError('Crop position must be in [0,1]')
        canvas.alpha_composite(ImageOps.fit(bg,box[2:],method=Image.Resampling.LANCZOS,centering=center),box[:2])
    records=[]; ids=set()
    for index,layer in enumerate(data['layers']):
        ident=layer.get('id',f'layer-{index}')
        if ident in ids:raise ValueError(f'Duplicate layer id: {ident}')
        ids.add(ident)
        x,y,w,h=checked_box(layer['box'],size)
        kind=layer.get('type','text')
        record={'id':ident,'type':kind,'box':[x,y,w,h]}
        if kind=='rect':
            d=ImageDraw.Draw(canvas)
            d.rounded_rectangle((x,y,x+w-1,y+h-1),radius=layer.get('radius',0),fill=layer['fill'])
        elif kind=='image':
            path=resolve(layer['path'])
            source=Image.open(path).convert('RGBA')
            if 'crop' in layer:
                crop=tuple(layer['crop'])
                if len(crop)!=4 or not(0<=crop[0]<crop[2]<=source.width and 0<=crop[1]<crop[3]<=source.height):
                    raise ValueError('Invalid source crop')
                source=source.crop(crop)
            fitted=ImageOps.contain(source,(w,h),method=Image.Resampling.LANCZOS)
            dx=(w-fitted.width)//2;dy=(h-fitted.height)//2
            canvas.alpha_composite(fitted,(x+dx,y+dy))
            record.update(path=str(path),render_box=[x+dx,y+dy,fitted.width,fitted.height],
                          source_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        elif kind=='text':
            face=Path(font_dir)/Path(layer['font']).name if font_dir else resolve(layer['font'])
            padding=int(layer.get('panel',{}).get('padding',0))
            if padding<0 or w<=2*padding or h<=2*padding:raise ValueError('Invalid panel padding')
            actual=int(layer['size']); minimum=int(layer.get('min_size',actual))
            if not 0<minimum<=actual:raise ValueError('Invalid font-size range')
            for actual in range(actual,minimum-1,-1):
                glyphs=typeset(layer['text'],face,actual,layer.get('tracking',0),layer.get('line_gap',0))
                if glyphs.width<=w-2*padding and glyphs.height<=h-2*padding:break
            else:raise ValueError(f'Text does not fit: {ident}')
            align=layer.get('align','left');valign=layer.get('valign','top')
            if align not in ('left','center','right') or valign not in ('top','center','bottom'):
                raise ValueError('Invalid alignment')
            dx={'left':padding,'center':(w-glyphs.width)/2,'right':w-padding-glyphs.width}[align]
            dy={'top':padding,'center':(h-glyphs.height)/2,'bottom':h-padding-glyphs.height}[valign]
            panel=layer.get('panel')
            if panel:
                ImageDraw.Draw(canvas).rounded_rectangle((x,y,x+w-1,y+h-1),radius=panel.get('radius',0),fill=panel['fill'])
            colored=Image.new('RGBA',glyphs.size,layer['fill'])
            colored.putalpha(glyphs.getchannel('A'))
            px,py=round(x+dx),round(y+dy)
            canvas.alpha_composite(colored,(px,py))
            record.update(text=layer['text'],font=str(face),size=actual,
                          tracking=layer.get('tracking',0),line_gap=layer.get('line_gap',0),
                          glyph_box=[px,py,px+glyphs.width,py+glyphs.height])
        else:raise ValueError(f'Unsupported layer type: {kind}')
        records.append(record)
    # Mandatory copy is compared after whitespace normalization, not by font geometry.
    normalize=lambda s:''.join(s.split())
    actual_text=''.join(normalize(r.get('text','')) for r in records)
    missing=[s for s in data.get('required_copy',[]) if normalize(s) not in actual_text]
    if missing:raise ValueError(f'Missing required copy: {missing}')
    output_path=Path(output_path).resolve()
    if output_path.suffix.lower()!='.png':raise ValueError('PNG output required')
    output_path.parent.mkdir(parents=True,exist_ok=True)
    canvas.convert('RGB').save(output_path)
    mobile_width=int(data.get('mobile_width',360))
    if mobile_width<=0:raise ValueError('Positive mobile width required')
    mobile=output_path.with_name(output_path.stem+'-mobile.png')
    canvas.convert('RGB').resize((mobile_width,round(size[1]*mobile_width/size[0])),Image.Resampling.LANCZOS).save(mobile)
    report={'config':str(config_path),'output':str(output_path),'size':list(size),
            'layer_order':[r['id'] for r in records],'layers':records,
            'required_copy':'passed','limitations':'Bounds and text presence do not verify product identity or visual quality.'}
    output_path.with_suffix('.render.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'output':str(output_path),'mobile':str(mobile),'layers':len(records)},ensure_ascii=False))
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--config',required=True)
    parser.add_argument('--output',required=True)
    parser.add_argument('--font-dir')
    args=parser.parse_args()
    render(args.config,args.output,args.font_dir)
