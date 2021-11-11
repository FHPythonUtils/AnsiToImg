""" tests """
import sys
from pathlib import Path

# For some reason stdout is reset in windows (might this be the work of
# colorama?) so save and reset...
oldStdout = sys.stdout

try:
	from catimage.catimage import generateHDColour
except ImportError:
	generateHDColour = lambda _name, _width: "😞\033[32mUnable to import catimage\033[0m"
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from ansitoimg.render import (
	ansiToHTML,
	ansiToHTMLRaster,
	ansiToRaster,
	ansiToSVG,
	ansiToSVGRaster,
)

# pylint:disable=invalid-name

# Define ANSI text
example = (
	"👋\033[32mHello\033[0m, \033[34mWorld\033[0m🌏\033[31m!\033[0m\n\033[41m"
	"👋\033[0m\033[43m🦄\033[0m\033[42m🐘\033[0m\033[3m\033[9m13\033[0m\033[1m3"
	"\033[0m\033[4m7\033[0m\033[46m🍄\033[0m\033[44m🎃\033[0m\033[45m🐦\033[0m"
)
example2 = (
	"hello\nworld\n\033[42m\033[31mwe meet again\033[0m\nABCDEFG"
	"HIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz😁😂🤣😃😄😅😆😉😊😋😎😍😘"
	"🥰😗😙😚☺🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪asdfghjk"
)
example3 = generateHDColour(f"{THISDIR}/test.png", 40)
with open(f"{THISDIR}/example4.txt", encoding="utf-8") as eg4:
	example4 = eg4.read()

sys.stdout = oldStdout

# Print
print(example)
print()
print(example2)
print()
print(example3)
print()
print(example4)
print()

# To SVG
ansiToSVG(example, f"{THISDIR}/example.svg", wide=False)
ansiToSVG(example2, f"{THISDIR}/example2.svg")
ansiToSVG(example3, f"{THISDIR}/example3.svg", wide=False)
ansiToSVG(example4, f"{THISDIR}/example4.svg", wide=False)

# To Raster
ansiToRaster(example, f"{THISDIR}/example.png", wide=False)
ansiToRaster(example2, f"{THISDIR}/example2.png")
ansiToRaster(example3, f"{THISDIR}/example3.png", wide=False)
ansiToRaster(example4, f"{THISDIR}/example4.png", wide=False)

# To SVGRaster
ansiToSVGRaster(example, f"{THISDIR}/svgExample.png", wide=False)
ansiToSVGRaster(example2, f"{THISDIR}/svgExample2.png")
ansiToSVGRaster(example3, f"{THISDIR}/svgExample3.png", wide=False)
ansiToSVGRaster(example4, f"{THISDIR}/svgExample4.png", wide=False)

# To HTML
ansiToHTML(example, f"{THISDIR}/example.html", wide=False)
ansiToHTML(example2, f"{THISDIR}/example2.html")
ansiToHTML(example3, f"{THISDIR}/example3.html", wide=False)
ansiToHTML(example4, f"{THISDIR}/example4.html", wide=False)

# To HTMLRaster
ansiToHTMLRaster(example, f"{THISDIR}/htmlExample.png", wide=False)
ansiToHTMLRaster(example2, f"{THISDIR}/htmlExample2.png")
ansiToHTMLRaster(example3, f"{THISDIR}/htmlExample3.png", wide=False)
ansiToHTMLRaster(example4, f"{THISDIR}/htmlExample4.png", wide=False)
