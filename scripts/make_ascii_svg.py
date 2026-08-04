# scripts/make_ascii_svg.py
from PIL import Image

RAMP = " .`:-=+*cs#%@"  # Sparse (light) to dense (dark)

def generate_ascii_svg(image_path="source-prepped.png", output_svg="ascii.svg", cols=100):
    img = Image.open(image_path).convert("L")
    w, h = img.size
    aspect_ratio = h / w
    rows = int(cols * aspect_ratio * 0.5)
    img = img.resize((cols, rows))
    
    lines = []
    for y in range(rows):
        line = ""
        for x in range(cols):
            pixel = img.getpixel((x, y))
            char = RAMP[int((pixel / 255) * (len(RAMP) - 1))]
            line += char if char != " " else "&#160;"
        lines.append(line)

    svg_lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="370" height="500" viewBox="0 0 370 500">',
        '<style>',
        '  .bg { fill: #0d1117; }',
        '  .ascii { font-family: monospace; font-size: 6px; fill: #8b949e; white-space: pre; }',
        '</style>',
        '<rect class="bg" width="100%" height="100%" rx="8"/>',
        '<text x="10" y="20" class="ascii">'
    ]
    
    for i, line in enumerate(lines):
        y_pos = 30 + (i * 7)
        svg_lines.append(f'<tspan x="10" y="{y_pos}">{line}</tspan>')
        
    svg_lines.append('</text></svg>')
    
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print(f"ASCII SVG generated at {output_svg}")

if __name__ == "__main__":
    generate_ascii_svg()