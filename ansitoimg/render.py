""" render the ansi

render as svg
"""
from pathlib import Path
import svgwrite
from yaml import safe_load
from ansitoimg.ansirep import AnsiBlocks, findLen

THISDIR = str(Path(__file__).resolve().parent)

# monospaced chars have a constant height and width
TEXT_HEIGHT = 15
TEXT_WIDTH = 8.7


def ansiToSVG(ansiText, fileName, theme=THISDIR + "/onedark.yml"):
	"""convert an ansi stream to svg

	Args:
		ansiText (string): ansi text to convert
		fileName (string): file path to svg to write
		theme (str, optional): file path to theme to use. Defaults to "onedark.yml".
	"""
	themeData = safe_load(open(theme))
	ansiBlocks = AnsiBlocks(ansiText)
	ansiBlocks.process()
	blocks = ansiBlocks.ansiBlocks
	size = (70 * TEXT_WIDTH, TEXT_HEIGHT * ansiBlocks.height + 5)
	dwg = svgwrite.Drawing(fileName, size)
	dwg.add(dwg.rect((0, 0), size, fill="#" + themeData["base00"]))
	group = dwg.g(style=
	"font-size:14px;font-family:FiraCode NF, Fira Code, Courier New, monospace;")
	for block in blocks:
		if block.bgColour is not None:
			group.add(
			dwg.rect((block.position[0] * TEXT_WIDTH + 5,
			block.position[1] * TEXT_HEIGHT + 2.5),
			(findLen(block.text) * 9.5, TEXT_HEIGHT), fill=block.bgColour))
		style = "" if any([
		block.bold, block.italic, block.underline, block.crossedOut]) else None
		if block.bold:
			style += "font-weight: bold;"
		if block.italic:
			style += "font-style: italic;"
		if block.underline:
			style += "text-decoration: underline;"
		if block.crossedOut:
			style += "text-decoration: line-through;"
		group.add(
		dwg.text(
		block.text, insert=(block.position[0] * TEXT_WIDTH + 5,
		(block.position[1] + 1) * TEXT_HEIGHT), fill=("#" + themeData["base05"]
		if block.fgColour is None else block.fgColour), style=style))
	dwg.add(group)
	dwg.save()
