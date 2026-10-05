with open('megha_about-life.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

# Left card
svg = svg.replace('Interfaces people remember', 'Systems, Data &amp; Mobile Apps')
svg = svg.replace('localhost:5173/megha', 'localhost:5173/sandib')

# Capability row 1
svg = svg.replace('Responsive, pixel-perfect UI', 'Production Android &amp; Jetpack Compose')
svg = svg.replace('HTML, CSS, JavaScript, React &amp; Bootstrap', 'Kotlin, MVVM, Room DB, Retrofit &amp; Modern UI')

# Capability row 2
svg = svg.replace('Motion that tells a story', 'Mutual Fund Analytics &amp; Pipelines')
svg = svg.replace('Scroll-driven scenes with GSAP &amp; Framer Motion', 'Python, SQLite Star Schema &amp; Financial Risk Metrics')

# Capability row 3
svg = svg.replace('Data &amp; enterprise workflows', 'Computer Vision &amp; Deep Learning')
svg = svg.replace('SQL queries and SAP-integrated business flows', 'OpenCV &amp; Keras Face Attendance System (CTTC Govt)')

# Right card
svg = svg.replace('Healthy body, curious mind', 'Curious mind, relentless builder')

# Carousel 1: HACK
svg = svg.replace('>RUN<', '>HACK<')
svg = svg.replace('>Health conscious<', '>State Hackathon 2nd<')
svg = svg.replace('Morning runs &amp; mindful habits fuel long build days.',
                  'Runner-Up at BPUT State Hackathon 2025 (GYANARATNA), pitching live tech.')

# Carousel 2: QUANT
svg = svg.replace('>SKATE<', '>QUANT<')
svg = svg.replace('>Weekend skater<', '>Market Analytics &amp; Data<')
svg = svg.replace('Balance on the board, balance in life.',
                  'Modeling financial data, star schemas &amp; quant performance metrics.')

# Carousel 3: DEV
svg = svg.replace('>ANIME<', '>DEV<')
svg = svg.replace('>Anime &amp; ramen<', '>Android &amp; Deep Tech<')
svg = svg.replace('Where most of my project ideas are born.',
                  'Exploring Gemini API, mobile architectures &amp; intelligent edge systems.')

# Daily rings
svg = svg.replace('>Move<', '>Build<')
svg = svg.replace('>Hydrate<', '>Analyze<')
# >Code< is kept

with open('about-life.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved about-life.svg successfully, size:", len(svg))
