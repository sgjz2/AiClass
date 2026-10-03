"""Render accurately positioned text over a generated advertising plate."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps


def render(config, output):
    config = Path(config).resolve()
    data = json.loads(config.read_text(encoding='utf-8-sig'))
    base = config.parent
    resolve = lambda p: Path(p) if Path(p).is_absolute() else base / p
    w, h = map(int, data['size'])
    if min(w, h) <= 0:
        raise ValueError('Canvas must have positive dimensions')
    background = Image.open(resolve(data['background'])).convert('RGB')
    if 'background_box' in data:
        bx,by,bw,bh = map(int,data['background_box'])
        if min(bx,by)<0 or min(bw,bh)<=0 or bx+bw>w or by+bh>h:
            raise ValueError('Background box outside canvas')
        center = tuple(data.get('crop_position',[.5,.5]))
        if len(center)!=2 or any(v<0 or v>1 for v in center):
            raise ValueError('Crop position must contain two values in [0,1]')
        canvas=Image.new('RGBA',(w,h),data.get('canvas_fill','#F4F2ED'))
        photo=ImageOps.fit(background,(bw,bh),method=Image.Resampling.LANCZOS,centering=center)
        canvas.paste(photo,(bx,by))
    else:
        if abs((background.width / background.height) / (w / h) - 1) > .02:
            raise ValueError('Background ratio differs >2%; choose an intentional crop first')
        canvas = ImageOps.fit(background, (w, h), method=Image.Resampling.LANCZOS).convert('RGBA')
    records = []
    for layer in data['layers']:
        x, y, bw, bh = map(int, layer['box'])
        if min(x, y) < 0 or min(bw, bh) <= 0 or x+bw > w or y+bh > h:
            raise ValueError(f'Layer box outside canvas: {layer["text"]}')
        if '\n' in layer['text']:
            raise ValueError('Use separate layers for multiline text')
        font_path = resolve(layer['font'])
        for size in range(int(layer['size']), int(layer.get('min_size', layer['size']))-1, -1):
            font = ImageFont.truetype(str(font_path), size)
            l, t, r, b = font.getbbox(layer['text'])
            if r-l <= bw and b-t <= bh:
                break
        else:
            raise ValueError(f'Text does not fit: {layer["text"]}')
        align = layer.get('align', 'left')
        valign = layer.get('valign', 'top')
        if align not in ('left', 'center', 'right') or valign not in ('top', 'center', 'bottom'):
            raise ValueError('Unsupported alignment')
        dx = {'left':0, 'center':(bw-(r-l))/2, 'right':bw-(r-l)}[align]
        dy = {'top':0, 'center':(bh-(b-t))/2, 'bottom':bh-(b-t)}[valign]
        overlay = Image.new('RGBA', (w, h))
        draw = ImageDraw.Draw(overlay)
        panel = layer.get('panel')
        if panel:
            draw.rounded_rectangle((x,y,x+bw,y+bh), radius=panel.get('radius',0), fill=panel['fill'])
            pad = panel.get('padding',0)
            if r-l > bw-2*pad or b-t > bh-2*pad:
                raise ValueError('Panel padding is insufficient')
        draw.text((x+dx-l,y+dy-t), layer['text'], font=font, fill=layer['fill'])
        canvas.alpha_composite(overlay)
        records.append({'text':layer['text'], 'font':str(font_path), 'size':size,
                        'glyph_box':[x+dx,y+dy,x+dx+r-l,y+dy+b-t], 'box':layer['box']})
    output = Path(output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert('RGB').save(output)
    mobile = output.with_name(output.stem+'-mobile.png')
    canvas.convert('RGB').resize((360,round(h*360/w)), Image.Resampling.LANCZOS).save(mobile)
    report = {'config':str(config),'output':str(output),'size':[w,h],'layers':records}
    output.with_suffix('.render.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'output':str(output),'mobile':str(mobile),'layers':len(records)},ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    render(args.config, args.output)
