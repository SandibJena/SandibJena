with open('megha_stack.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

# Replace header categories
svg = svg.replace('Tools I build with', 'Technologies &amp; frameworks I build with')
svg = svg.replace('>FRONTEND<', '>MOBILE &amp; FRONTEND<')
svg = svg.replace('>MOTION &amp; 3D<', '>DATA &amp; QUANT ANALYTICS<')
svg = svg.replace('>DATA &amp; ENTERPRISE<', '>AI / ML &amp; COMPUTER VISION<')
svg = svg.replace('>AI &amp; WORKFLOW<', '>DEV TOOLS &amp; ARCHITECTURE<')

# Chips row 1 (Mobile & Frontend):
# HTML5 -> Kotlin
svg = svg.replace('>HTML5<', '>Kotlin<')
# CSS -> Java
svg = svg.replace('>CSS<', '>Java<')
# JavaScript -> Jetpack Compose
svg = svg.replace('>JavaScript<', '>Compose<')
# TypeScript -> Room DB
svg = svg.replace('>TypeScript<', '>XML UI<')
# React -> React
# Bootstrap -> HTML/CSS
svg = svg.replace('>Bootstrap<', '>HTML/CSS<')

# Chips row 2 (Data & Quant Analytics):
# GSAP -> Python
svg = svg.replace('>GSAP<', '>Python<')
# Framer -> SQLite
svg = svg.replace('>Framer<', '>SQLite Star<')
# Three.js -> Pandas
svg = svg.replace('>Three.js<', '>Pandas &amp; NumPy<')

# Chips row 3 (AI / ML & CV):
# SQL -> OpenCV
svg = svg.replace('>SQL<', '>OpenCV<')
# SAP -> Keras / TF
svg = svg.replace('>SAP<', '>Keras CV<')

# Chips row 4 (Dev Tools & Architecture):
# Claude -> Gemini API
svg = svg.replace('>Claude<', '>Gemini API<')
# GitHub Copilot -> Vertex AI
svg = svg.replace('>GitHub Copilot<', '>Vertex AI<')
# AI Prompting -> MVVM / Room
svg = svg.replace('>AI Prompting<', '>MVVM / Room<')
# Git -> Git
# GitHub -> GitHub

with open('stack.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved stack.svg successfully, size:", len(svg))
