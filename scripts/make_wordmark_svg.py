import os

def generate_wordmark_svg():
    # 3D Extruded ASCII Banner for SAKETH (5 lines)
    ascii_banner = [
        r"  ____     _     _  __ _____ _______ ___    ___",
        r" / ___|   / \   | |/ /| ____ |_   _| | |    | |",
        r" \___ \  / _ \  | ' / |  _|    | |   | |____| |",
        r"  ___)| / ___ \ | . \ | |___   | |   | |----| |",
        r" |____/|_/   \_||_|\_||_____|  |_|   |_|    |_|"  
    ]

    # Pre-render Front Layer ASCII Lines
    front_tspans = []
    y_pos = 75
    for line in ascii_banner:
        front_tspans.append(f'    <tspan x="20" y="{y_pos}">{line}</tspan>')
        y_pos += 12
    front_ascii = "\n".join(front_tspans)

    # Keyframe Offsets (dx, dy) simulating 12 discrete orbit positions around origin (20, Y)
    orbit_positions = [
        (0, 2),   # Frame 0
        (3, 2),   # Frame 1
        (5, 1),   # Frame 2
        (6, 0),   # Frame 3
        (5, -1),  # Frame 4
        (3, -2),  # Frame 5
        (0, -2),  # Frame 6
        (-3, -2), # Frame 7
        (-5, -1), # Frame 8
        (-6, 0),  # Frame 9
        (-5, 1),  # Frame 10
        (-3, 2)   # Frame 11
    ]

    num_frames = len(orbit_positions)
    frames_svg = []

    for i, (dx, dy) in enumerate(orbit_positions):
        # Generate keyTimes array: e.g., "0;0.083;0.166;..."
        key_times = ";".join([f"{j / num_frames:.3f}".rstrip('0').rstrip('.') for j in range(num_frames)])
        
        # Binary opacity map: '1' at frame i, '0' everywhere else
        opacity_vals = [ "1" if j == i else "0" for j in range(num_frames) ]
        opacity_pattern = ";".join(opacity_vals)

        # Build tspan elements with offset coordinates
        tspans = []
        base_y = 75 + dy
        base_x = 20 + dx
        for line in ascii_banner:
            tspans.append(f'      <tspan x="{base_x}" y="{base_y}">{line}</tspan>')
            base_y += 12

        frame_ascii = "\n".join(tspans)

        # Initial opacity state for Frame 0 vs others
        init_opacity = "1" if i == 0 else "0"

        frame_block = f'''  <!-- Frame {i} -->
  <g opacity="{init_opacity}">
    <animate attributeName="opacity" calcMode="discrete" values="{opacity_pattern}" keyTimes="{key_times}" dur="4s" repeatCount="indefinite" begin="1.6s"/>
    <text fill="#1f6beb" font-size="10" opacity="0.6" xml:space="preserve">
{frame_ascii}
    </text>
  </g>'''
        frames_svg.append(frame_block)

    all_frames_content = "\n\n".join(frames_svg)

    # Complete SVG Document Construction
    svg_content = f'''<svg width="486" height="387" viewBox="0 0 486 387" fill="none" xmlns="http://www.w3.org/2000/svg">
<style>
text {{
  font-family: 'Fira Code', Monaco, Consolas, 'Ubuntu Mono', 'Liberation Mono', 'Courier New', monospace;
}}
</style>

<clipPath id="wipe">
  <rect x="0" y="0" width="0" height="387">
    <animate attributeName="width" values="0;486" dur="1.6s" fill="freeze" keyTimes="0;1" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
  </rect>
</clipPath>

<linearGradient id="bg" x1="0" y1="0" x2="0" y2="387" gradientUnits="userSpaceOnUse">
  <stop stop-color="#111722"/>
  <stop offset="1" stop-color="#0d1117"/>
</linearGradient>

<!-- Window Frame -->
<rect width="486" height="387" rx="12" fill="url(#bg)"/>
<rect x="0.5" y="0.5" width="485" height="386" rx="11.5" stroke="#30363d" stroke-opacity="0.8"/>

<!-- Window Controls Bar -->
<path d="M0 12C0 5.37258 5.37258 0 12 0H474C480.627 0 486 5.37258 486 12V38H0V12Z" fill="#161b22"/>
<line x1="0" y1="38.5" x2="486" y2="38.5" stroke="#30363d" stroke-opacity="0.8"/>
<circle cx="18" cy="19" r="5" fill="#ff5f56"/>
<circle cx="34" cy="19" r="5" fill="#ffbd2e"/>
<circle cx="50" cy="19" r="5" fill="#27c93f"/>
<text x="243" y="23" fill="#8b949e" font-size="12" text-anchor="middle">saketh@github: ~$ ./wordmark.sh --3d</text>

<g clip-path="url(#wipe)">
{all_frames_content}

  <!-- STEADY FRONT LAYER -->
  <text fill="#58a6ff" font-size="10" xml:space="preserve">
{front_ascii}
  </text>

  <!-- Terminal Info & Details -->
  <text x="20" y="160" fill="#8b949e" font-size="12">
    <tspan fill="#3fb950">saketh@github</tspan>:<tspan fill="#58a6ff">~</tspan>$ neofetch
  </text>
  
  <text x="20" y="185" fill="#c9d1d9" font-size="11">
    <tspan fill="#58a6ff">OS</tspan>: macOS / Arch Linux
  </text>
  <text x="20" y="205" fill="#c9d1d9" font-size="11">
    <tspan fill="#58a6ff">Focus</tspan>: Machine Learning &amp; Computer Vision
  </text>
  <text x="20" y="225" fill="#c9d1d9" font-size="11">
    <tspan fill="#58a6ff">Stack</tspan>: Python, PyTorch, C++, CUDA
  </text>
  <text x="20" y="245" fill="#c9d1d9" font-size="11">
    <tspan fill="#58a6ff">Status</tspan>: Building intelligent systems...
  </text>

  <!-- Active Prompt Line with Blinking Cursor -->
  <text x="20" y="285" fill="#8b949e" font-size="12">
    <tspan fill="#3fb950">saketh@github</tspan>:<tspan fill="#58a6ff">~</tspan>$ <tspan fill="#c9d1d9">_</tspan>
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </text>
</g>
</svg>'''

    with open("wordmark.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Successfully generated wordmark.svg!")

if __name__ == "__main__":
    generate_wordmark_svg()
