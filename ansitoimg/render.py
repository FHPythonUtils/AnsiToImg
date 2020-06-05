""" render the ansi

render as svg
"""
import asyncio
from os import remove
from pathlib import Path
import svgwrite
from yaml import safe_load
from PIL import Image, ImageDraw, ImageFont
from pyppeteer import launch
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
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
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


def ansiToRaster(ansiText, fileName, theme=THISDIR + "/onedark.yml"):
	"""convert an ansi stream to a raster image with pillow

	Args:
		ansiText (string): ansi text to convert
		fileName (string): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
	"""
	themeData = safe_load(open(theme))
	ansiBlocks = AnsiBlocks(ansiText)
	ansiBlocks.process()
	blocks = ansiBlocks.ansiBlocks
	size = (int(70 * TEXT_WIDTH), int(TEXT_HEIGHT * ansiBlocks.height + 5))
	image = Image.new("RGB", size, "#" + themeData["base00"])
	draw = ImageDraw.Draw(image)
	# Load the fonts
	fontNormal = ImageFont.truetype(THISDIR + "/resources/FiraCode-Regular.otf",
	14)
	fontBold = ImageFont.truetype(THISDIR + "/resources/FiraCode-Bold.otf", 14)
	fontItalic = ImageFont.truetype(THISDIR + "/resources/FiraCode-Italic.otf",
	14)
	fontBoldItalic = ImageFont.truetype(
	THISDIR + "/resources/FiraCode-BoldItalic.otf", 14)
	fontEmoji = ImageFont.truetype(
	THISDIR + "/resources/TwitterColorEmoji-SVGinOT30.ttf", 14)
	# Iterate through the ansi blocks
	for block in blocks:
		posY = block.position[1] * TEXT_HEIGHT + 2.5
		if block.bgColour is not None:
			posX = block.position[0] * TEXT_WIDTH + 5
			draw.rectangle((posX, posY, posX + findLen(block.text) * 9.5,
			posY + TEXT_HEIGHT), block.bgColour)
		text = block.text
		font = fontNormal
		fill = ("#" + themeData["base05"]
		if block.fgColour is None else block.fgColour) # get the block fill colour
		if block.bold and block.italic:
			font = fontBoldItalic
		elif block.bold:
			font = fontBold
		elif block.italic:
			font = fontItalic
		index = 0
		for char in text:
			posX = (block.position[0] + index) * TEXT_WIDTH + 5
			if ord(char) > 10000: # I wish there was a better way of doing this...
				draw.text((posX, posY + 2), char, font=fontEmoji, fill=fill)
				index += 2
			else:
				draw.text((posX, posY), char if not block.crossedOut else '\u0336' + char +
				'\u0336', font=font, fill=fill)
				index += 1
			if block.underline:
				draw.line((posX, posY + TEXT_HEIGHT, posX + 9.5, posY + TEXT_HEIGHT),
				fill=fill, width=1)
	image.save(fileName)


def ansiToSVGRaster(ansiText, fileName, theme=THISDIR + "/onedark.yml"):
	"""convert an ansi stream to a raster image using pypeteer to take a
	screenshot of a generated svg (hacky but we can get coloured emoji now)

	Args:
		ansiText (string): ansi text to convert
		fileName (string): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
	"""
	ansiToSVG(ansiText, THISDIR + "/temp.svg", theme)
	ansiBlocks = AnsiBlocks(ansiText)
	ansiBlocks.process()
	size = (int(70 * TEXT_WIDTH), int(TEXT_HEIGHT * ansiBlocks.height + 5))
	asyncio.get_event_loop().run_until_complete(
	_doGrabWebpage('file:///' + THISDIR + "/temp.svg", size, fileName))
	try:
		remove(THISDIR + "/temp.svg")
	except PermissionError:
		print("Unable to clean up, manually remove temp.svg from project root " +
		"or ignore")


async def _doGrabWebpage(url, resolution, fileName):
	''' Go to a URL, with a browser with a set resolution and take a screenshot'''
	browser = await launch(
	options={'args': ['--no-sandbox', '--disable-web-security']})
	page = await browser.newPage()
	await page.setViewport({"width": resolution[0], "height": resolution[1]})
	await page.goto(url)
	await page.screenshot({'path': fileName})
	await browser.close()
