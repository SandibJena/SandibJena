import re
import base64
from io import BytesIO
from PIL import Image

# 1. Prepare pointing character PNG as base64
im = Image.open('pointing_character.png')
# Quantize to 256 colors for fast SVG loading while retaining sharp graphics
im_quant = im.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
buf = BytesIO()
im_quant.save(buf, format='PNG', optimize=True)
b64_pointing = base64.b64encode(buf.getvalue()).decode('ascii')
data_uri = f"data:image/png;base64,{b64_pointing}"
print(f"Pointing char b64 size: {len(data_uri)} bytes")

# 2. Read template megha_connect.svg
with open('megha_connect.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

# Replace image
svg = re.sub(r'<image\s+x="70"\s+y="36"[^>]+>',
             f'<image x="70" y="36" width="368" height="424" href="{data_uri}" preserveAspectRatio="xMidYMax meet"/>',
             svg)

# Replace description
svg = svg.replace('<desc>Megha pointing at her handle, beside cards linking to GitHub, email, Instagram and Threads.</desc>',
                  '<desc>Sandib pointing at his handle, beside cards linking to GitHub, Email, LinkedIn and Phone.</desc>')

# Subtitle
svg = svg.replace('Open to collabs, freelance work and anime-sized ideas.',
                  'Open to collabs, technical roles, data pipelines &amp; Android engineering.')

# Card 1: GitHub
svg = svg.replace('Meghamittal0920', 'SandibJena')

# Card 2: Email
svg = svg.replace('meghamittal563@gmail.com', 'jenasandib@gmail.com')

# Card 3: Replace Instagram with LinkedIn
# Search Instagram card block
old_card3 = re.search(r'<g class="card" style="animation-delay:1\.14.*?Instagram.*?</g>', svg, re.DOTALL)
if old_card3:
    print("Found Instagram card!")
    # Replace Instagram title and handle
    new_card3 = old_card3.group(0).replace('Instagram', 'LinkedIn').replace('@meghamittal92000', 'in/sandibjena')
    # Replace Instagram SVG icon with LinkedIn SVG icon
    linkedin_icon = '<path fill="#0077b5" transform="scale(1)" d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>'
    new_card3 = re.sub(r'<path fill="#FF0069"[^>]+d="[^"]+"', linkedin_icon, new_card3)
    svg = svg.replace(old_card3.group(0), new_card3)

# Card 4: Replace Threads with Phone / WhatsApp
old_card4 = re.search(r'<g class="card" style="animation-delay:1\.26.*?Threads.*?</g>', svg, re.DOTALL)
if old_card4:
    print("Found Threads card!")
    new_card4 = old_card4.group(0).replace('Threads', 'Phone / WhatsApp').replace('@meghamittal92000', '+91 9348441103')
    phone_icon = '<path fill="#34d399" transform="scale(1)" d="M20 15.5c-1.25 0-2.45-.2-3.57-.57a1 1 0 0 0-1.02.24l-2.2 2.2a15.05 15.05 0 0 1-6.59-6.59l2.2-2.21a1 1 0 0 0 .25-1.02A11.36 11.36 0 0 1 8.5 4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1z"/>'
    new_card4 = re.sub(r'<path fill="#eceef6"[^>]+d="[^"]+"', phone_icon, new_card4)
    svg = svg.replace(old_card4.group(0), new_card4)

# Replace quote
svg = svg.replace('Code is my art, logic is my superpower.',
                  'Driven by data, engineered for performance, designed to scale.')

with open('connect.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved connect.svg successfully, size:", len(svg))
