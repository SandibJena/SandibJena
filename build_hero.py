import re
import base64
from io import BytesIO
from PIL import Image

# 1. Prepare hero character base64
im = Image.open('hero_character.png')
im_quant = im.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
buf = BytesIO()
im_quant.save(buf, format='PNG', optimize=True)
b64_hero = base64.b64encode(buf.getvalue()).decode('ascii')
data_uri = f"data:image/png;base64,{b64_hero}"
print(f"Hero image b64 size: {len(data_uri)} bytes")

# 2. Read template megha_hero.svg
with open('megha_hero.svg', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<!-- VIDEO -->' in line:
        new_lines.append('  <!-- VIDEO / VIEWPORT -->\n')
        new_lines.append('  <g mask="url(#vmask)"><g mask="url(#vmaskB)">\n')
        new_lines.append('    <g>\n')
        new_lines.append('      <animateTransform attributeName="transform" type="translate" values="0 0; 0 -6; 0 0" dur="4.0s" repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .2 1; .4 0 .2 1"/>\n')
        new_lines.append(f'      <image x="560" y="0" width="724" height="540" href="{data_uri}" preserveAspectRatio="xMidYMid meet"/>\n')
        new_lines.append('    </g>\n')
        new_lines.append('  </g></g>\n')
        skip = True
        continue
    if skip:
        if '<!-- viewfinder HUD -->' in line:
            skip = False
            new_lines.append(line)
        continue
    new_lines.append(line)

svg = "".join(new_lines)

# Metadata / Accessibility
svg = svg.replace('aria-label="Megha Mittal — Frontend Developer"',
                  'aria-label="Sandib Jena — Data Analyst &amp; Android Developer"')
svg = svg.replace('<title>Megha Mittal — Frontend Developer</title>',
                  '<title>Sandib Jena — Data Analyst &amp; Android Developer</title>')
svg = svg.replace('<desc>Animated hero: Megha walks in and waves hi, next to her name, cycling roles and details.</desc>',
                  '<desc>Animated hero: Sandib Jena holding laptop, next to his name, cycling roles and details.</desc>')

# HUD text
svg = svg.replace('HELLO.MP4 &#183; 24FPS', 'DEV_STREAM.RAW &#183; 60FPS')

# Name
svg = svg.replace('Megha Mittal', 'Sandib Jena')

# Roles
svg = svg.replace('Frontend Developer', 'Data Analyst &amp; Engineer')
svg = svg.replace('Motion &amp; GSAP Animator', 'Android &amp; Compose Dev')
svg = svg.replace('Anime Web Experiences', 'Quant Analytics &amp; Pipelines')
svg = svg.replace('AI-Assisted Builder', 'AI &amp; Computer Vision Explorer')

# Pitch
svg = svg.replace('Crafting fast, responsive interfaces and cinematic,',
                  'Engineering high-throughput data pipelines, star schema ETLs,')
svg = svg.replace('anime-inspired web experiences with React &amp; GSAP.',
                  'and production Android apps with clean architecture &amp; Gemini AI.')

# Badges
svg = svg.replace('Noida, India', 'Balasore, India')
svg = svg.replace('Wiley', 'GCEK / Bluestock')
svg = svg.replace('54 stars &#183; 8 repos', '14+ repos &#183; 500+ commits')

with open('hero.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved hero.svg successfully, size:", len(svg))
