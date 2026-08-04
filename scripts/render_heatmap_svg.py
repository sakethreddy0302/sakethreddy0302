# scripts/render_heatmap_svg.py
import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render(json_path="data/contributions.json", output_svg="contrib-heatmap.svg"):
    with open(json_path) as f:
        days = json.load(f)
        
    svg_lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="860" height="150" viewBox="0 0 860 150">',
        '<style>',
        '  .bg { fill: #0d1117; rx: 8px; }',
        '  .day { rx: 2px; animation: fadeIn 0.3s ease-in-out forwards; opacity: 0; }',
        '  @keyframes fadeIn { to { opacity: 1; } }',
        '</style>',
        '<rect class="bg" width="100%" height="100%"/>',
        '<g transform="translate(20, 20)">'
    ]
    
    for idx, day in enumerate(days):
        week = idx // 7
        day_of_week = idx % 7
        x = week * 15
        y = day_of_week * 15
        color = PALETTE[min(day["level"], 5)]
        delay = (week + day_of_week) * 0.02
        
        svg_lines.append(
            f'<rect class="day" x="{x}" y="{y}" width="11" height="11" fill="{color}" style="animation-delay: {delay:.2f}s"/>'
        )
        
    svg_lines.append('</g></svg>')
    
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    print(f"Heatmap rendered to {output_svg}")

if __name__ == "__main__":
    render()