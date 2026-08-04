import os

def generate_wordmark_svg():
    # 3D Extruded ASCII Banner for SAKETH
    ascii_banner = [
        r"  ____     _     _  _____ _____ _____    __ ",
        r" / ___|   / \   | |/ /| ____|_   _| ||    ||",
        r" \___ \  / _ \  | ' / |  _|   | |   ||____||",
        r"  ___)| / ___ \ | . \ | |___  | |   ||----||",
        r" |____/|_/   \_||_|\_||_____| |_|   ||    ||"
    ]

    # Convert ASCII text into SVG text spans with styling
    text_lines = []
    y_pos = 65
    for line in ascii_banner:
        # Escape XML special characters
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&#160;')
        text_lines.append(f'<tspan x="20" y="{y_pos}">{escaped_line}</tspan>')
        y_pos += 22

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 200" width="100%" height="100%">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; }}
    .ascii-text {{
      font-family: 'Courier New', Courier, monospace;
      font-size: 14px;
      font-weight: bold;
      fill: #58a6ff;
      filter: drop-shadow(2px 2px 0px #1f6feb);
    }}
    .subtext {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 13px;
      fill: #8b949e;
    }}
  </style>
  <rect width="100%" height="100%" class="bg" />
  <text class="ascii-text">
    {''.join(text_lines)}
  </text>
  <text x="20" y="175" class="subtext">software engineer • machine learning • developer</text>
</svg>'''

    with open("wordmark.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Successfully generated wordmark.svg!")

if __name__ == "__main__":
    generate_wordmark_svg()
