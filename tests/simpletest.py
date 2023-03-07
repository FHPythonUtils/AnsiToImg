""" tests """
from __future__ import annotations

import sys
from pathlib import Path

# For some reason stdout is reset in windows (might this be the work of
# colorama?) so save and reset...
oldStdout = sys.stdout

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from ansitoimg.render import (
	ansiToHTML,
	ansiToHTMLRender,
	ansiToRender,
	ansiToSVG,
	ansiToSVGRender,
)

# pylint:disable=invalid-name

# Define ANSI text
fancyHelloWorld = (
	"👋\033[32mHello\033[0m, \033[34mWorld\033[0m🌏\033[31m!\033[0m\n\033[41m"
	"👋\033[0m\033[43m🦄\033[0m\033[42m🐘\033[0m\033[3m\033[9m13\033[0m\033[1m3"
	"\033[0m\033[4m7\033[0m\033[46m🍄\033[0m\033[44m🎃\033[0m\033[45m🐦\033[0m"
)
fredHappyfaceHD = Path(f"{THISDIR}/data/fredHappyfaceHD.txt").read_text(encoding="utf-8")
cat = Path(f"{THISDIR}/data/cat.txt").read_text(encoding="utf-8")
sys.stdout = oldStdout

# Print
print(fancyHelloWorld)
print()
print(fredHappyfaceHD)
print()
print(cat)
print()

# To SVG
ansiToSVG(fancyHelloWorld, f"{THISDIR}/data/fancyHelloWorld.svg", wide=False)
ansiToSVG(fredHappyfaceHD, f"{THISDIR}/data/fredHappyfaceHD.svg")
ansiToSVG(cat, f"{THISDIR}/data/cat.svg", width=100)

# To Render
ansiToRender(fancyHelloWorld, f"{THISDIR}/data/fancyHelloWorld.png", wide=False)
ansiToRender(fredHappyfaceHD, f"{THISDIR}/data/fredHappyfaceHD.png")
ansiToRender(cat, f"{THISDIR}/data/cat.png", width=100)

# To SVGRender
ansiToSVGRender(fancyHelloWorld, f"{THISDIR}/data/fancyHelloWorld.svg.png", wide=False)
ansiToSVGRender(fredHappyfaceHD, f"{THISDIR}/data/fredHappyfaceHD.svg.png")
ansiToSVGRender(cat, f"{THISDIR}/data/cat.svg.png", width=100)

# To HTML
ansiToHTML(fancyHelloWorld, f"{THISDIR}/data/fancyHelloWorld.html", wide=False)
ansiToHTML(fredHappyfaceHD, f"{THISDIR}/data/fredHappyfaceHD.html")
ansiToHTML(cat, f"{THISDIR}/data/cat.html", width=100)

# To HTMLRender
ansiToHTMLRender(fancyHelloWorld, f"{THISDIR}/data/fancyHelloWorld.html.png", wide=False)
ansiToHTMLRender(fredHappyfaceHD, f"{THISDIR}/data/fredHappyfaceHD.html.png")
ansiToHTMLRender(metprintOutput, f"{THISDIR}/data/metprintOutput.html.png", wide=False)
ansiToHTMLRender(cat, f"{THISDIR}/data/cat.html.png", width=100)

# To SVGRender 06/03/2023
ansiToSVGRender(fancyHelloWorld, f"{THISDIR}/data/hw20.svg.png", width=20)
ansiToSVGRender(fancyHelloWorld, f"{THISDIR}/data/hwT20.svg.png", wide=True, width=20)
ansiToSVGRender(fancyHelloWorld, f"{THISDIR}/data/hw40test.svg.png", width=40, title="test")
