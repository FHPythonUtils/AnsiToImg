""" tests """
import sys
import os
from pathlib import Path

# For some reason stdout is reset in windows (might this be the work of
# colorama?) so save and reset...
oldStdout = sys.stdout

from catimage.catimage import generateHDColour

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from ansitoimg.render import ansiToSVG, ansiToRaster, ansiToSVGRaster, ansiToHTML, ansiToHTMLRaster


# Define ANSI text
example = "👋\033[32mHello\033[0m, \033[34mWorld\033[0m🌏\033[31m!\033[0m\n\033[41m👋\033[0m\033[43m🦄\033[0m\033[42m🐘\033[0m\033[3m\033[9m13\033[0m\033[1m3\033[0m\033[4m7\033[0m\033[46m🍄\033[0m\033[44m🎃\033[0m\033[45m🐦\033[0m"
example2 = "hello\nworld\n\033[42m\033[31mwe meet again\033[0m\nABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗😙😚☺🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪asdfghjk"
example3 = generateHDColour(THISDIR + "/test.png", 40)
example4 = open(THISDIR + "/example4.txt", "r", encoding="utf-8").read()

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
ansiToSVG(example, THISDIR + "/example.svg", wide=False)
ansiToSVG(example2, THISDIR + "/example2.svg")
ansiToSVG(example3, THISDIR + "/example3.svg", wide=False)
ansiToSVG(example4, THISDIR + "/example4.svg", wide=False)

# To Raster
ansiToRaster(example, THISDIR + "/example.png", wide=False)
ansiToRaster(example2, THISDIR + "/example2.png")
ansiToRaster(example3, THISDIR + "/example3.png", wide=False)
ansiToRaster(example4, THISDIR + "/example4.png", wide=False)

# To SVGRaster
ansiToSVGRaster(example, THISDIR + "/svgExample.png", wide=False)
ansiToSVGRaster(example2, THISDIR + "/svgExample2.png")
ansiToSVGRaster(example3, THISDIR + "/svgExample3.png", wide=False)
ansiToSVGRaster(example4, THISDIR + "/svgExample4.png", wide=False)

# To HTML
ansiToHTML(example, THISDIR + "/example.html", wide=False)
ansiToHTML(example2, THISDIR + "/example2.html")
ansiToHTML(example3, THISDIR + "/example3.html", wide=False)
ansiToHTML(example4, THISDIR + "/example4.html", wide=False)

# To HTMLRaster
ansiToHTMLRaster(example, THISDIR + "/htmlExample.png", wide=False)
ansiToHTMLRaster(example2, THISDIR + "/htmlExample2.png")
ansiToHTMLRaster(example3, THISDIR + "/htmlExample3.png", wide=False)
ansiToHTMLRaster(example4, THISDIR + "/htmlExample4.png", wide=False)
