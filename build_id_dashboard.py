import re
import base64
from io import BytesIO
from PIL import Image

# 1. Prepare portrait character PNG as base64 for ID card (136x168)
im = Image.open('portrait_character.png')
# Crop or resize to fit 136x168 nicely
# The portrait is (605, 682). Let's take upper body/face for the ID badge
w, h = im.size
crop_box = (int(w * 0.15), int(h * 0.05), int(w * 0.85), int(h * 0.85))
cropped = im.crop(crop_box)
resized = cropped.resize((136, 168), Image.Resampling.LANCZOS)
im_quant = resized.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
buf = BytesIO()
im_quant.save(buf, format='PNG', optimize=True)
b64_portrait = base64.b64encode(buf.getvalue()).decode('ascii')
data_uri = f"data:image/png;base64,{b64_portrait}"
print(f"ID photo b64 size: {len(data_uri)} bytes")

# 2. Read template megha_id-dashboard.svg
with open('megha_id-dashboard.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

# Replace photo
svg = re.sub(r'<image\s+x="144"\s+y="204"[^>]+>',
             f'<image x="144" y="204" width="136" height="168" href="{data_uri}" preserveAspectRatio="xMidYMin slice"/>',
             svg)

# Replace description
svg = svg.replace('Megha', 'Sandib')

# Lanyard strap
svg = svg.replace('MEGHA.DEV &#183; FRONTEND &#183; MEGHA.DEV &#183; FRONTEND',
                  'SANDIB JENA &#183; DATA &amp; ANDROID &#183; GCEK &#183; BLUESTOCK')

# ID card text
svg = svg.replace('Megha Mittal', 'Sandib Jena')
svg = svg.replace('FRONTEND DEVELOPER', 'DATA &amp; ANDROID DEV')
svg = svg.replace('Noida, IN', 'Balasore, IN')
svg = svg.replace('Wiley', 'Bluestock')
svg = svg.replace('MM-0920', 'SJ-2024-28')
svg = svg.replace('2022', '2024')
svg = svg.replace('@Meghamittal0920', '@SandibJena')

# Tile 1: PUBLIC REPOS (animate up to 14)
# Current values in template: 0, 2, 4, 6, 8
svg = svg.replace('>8<animate', '>14<animate')
svg = svg.replace('>6<animate', '>10<animate')
svg = svg.replace('>4<animate', '>7<animate')
svg = svg.replace('>2<animate', '>3<animate')

# Tile 2: BPUT STATE HACKATHON 2nd Prize (gold star icon already exists!)
# Current template: 0, 13, 27, 43, 54 TOTAL STARS
svg = svg.replace('TOTAL STARS', 'BPUT HACKATHON')
svg = svg.replace('>54<animate', '>2nd<animate')
svg = svg.replace('>43<animate', '>2nd<animate')
svg = svg.replace('>27<animate', '>Top 3<animate')
svg = svg.replace('>13<animate', '>Top 10<animate')

# Tile 3: PRODUCTION APPS
# Current template: 0, 5, 11, 18, 23 FORKS
svg = svg.replace('FORKS', 'APPS SHIPPED')
svg = svg.replace('>23<animate', '>4<animate')
svg = svg.replace('>18<animate', '>3<animate')
svg = svg.replace('>11<animate', '>2<animate')
svg = svg.replace('>5<animate', '>1<animate')

# Tile 4: COMMITS / CODE
# Current template: 0, 6, 12, 20, 25 FOLLOWERS
svg = svg.replace('FOLLOWERS', 'COMMITS (2026)')
svg = svg.replace('>25<animate', '>500+<animate')
svg = svg.replace('>20<animate', '>400<animate')
svg = svg.replace('>12<animate', '>250<animate')
svg = svg.replace('>6<animate', '>100<animate')

# Project bars
svg = svg.replace('Naruto — Sage Mode', 'Mutual Fund Analytics')
svg = svg.replace('>25<animate', '>98%<animate')

svg = svg.replace('Zoro — King of Hell', 'Gyanaratna AI App')
svg = svg.replace('>9<animate', '>2nd<animate')

svg = svg.replace('Demon Slayer', 'Face Attendance CV')
svg = svg.replace('>8<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8905"',
                  '>99%<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8905"')

svg = svg.replace('JJK — Sukuna', 'CALCY Android Suite')
svg = svg.replace('>8<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8951"',
                  '>4 Apps<animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.8951"')

svg = svg.replace('One Piece 3D', 'ResumeForge AI')
svg = svg.replace('>2<animate', '>v1.0<animate')

svg = svg.replace('stars per repository &#183; anime web builds',
                  'key builds &#183; mutual fund etl, cv &amp; android suite')

# Community tile
svg = svg.replace('4.7K', '1.2K+')
svg = svg.replace('IG FOLLOWERS', 'CONNECTIONS')
svg = svg.replace('2.7M', '100%')
svg = svg.replace('VIEWS / 30 DAYS', 'DEDICATION')
svg = svg.replace('@meghamittal92000', 'linkedin/in/sandibjena')

# Building/Exploring tile
svg = svg.replace('Cinematic anime web experiences',
                  'Mutual fund analytics &amp; star schema ETL')
svg = svg.replace('3D on the web &amp; AI pair-programming',
                  'Gemini API, Vertex AI &amp; Deep Learning CV')
svg = svg.replace('Coffee, ramen &amp; morning runs',
                  'Clean code, quant finance &amp; hackathons')

with open('id-dashboard.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved id-dashboard.svg successfully, size:", len(svg))
