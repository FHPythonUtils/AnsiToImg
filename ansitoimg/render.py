""" render the ANSI

render as SVG
"""
from __future__ import annotations
from typing import Optional

import asyncio
from os import remove
from pathlib import Path
import svgwrite
from yaml import safe_load
from PIL import Image, ImageDraw, ImageFont
from pyppeteer import launch
from markupsafe import escape
from ansitoimg.ansirep import AnsiBlocks, findLen

THISDIR = str(Path(__file__).resolve().parent)

# monospaced chars have a constant height and width
TEXT_HEIGHT = 15
TEXT_WIDTH = 8.7


def ansiToSVG(ansiText: str, fileName: str, theme: Optional[str]=None, wide: bool=True):
	"""convert an ANSI stream to SVG

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): file path to SVG to write
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
	"""
	themeData = safe_load(open(theme if theme is not None else THISDIR + "/onedark.yml"))
	ansiBlocks = AnsiBlocks(ansiText, wide)
	ansiBlocks.process()
	blocks = ansiBlocks.ansiBlocks
	size = ((95 if wide else 55) * TEXT_WIDTH, TEXT_HEIGHT * ansiBlocks.height + 5)
	dwg = svgwrite.Drawing(fileName, size)
	dwg.add(dwg.rect((0, 0), size, fill="#" + themeData["base00"])) # type: ignore
	dwg.defs.add(dwg.style("@import url('https://rawcdn.githack.com/tonsky/FiraCode/07666484a9d92ec6ea916b94f776fc2410a87a11/distr/fira_code.css');"))
	group = dwg.g(style="font-weight:300;font-size:14.15px;font-family:FiraCode NF, Fira Code, " +
	"Cousine, Courier New, monospace;")
	for block in blocks:
		if block.bgColour is not None:
			group.add(
			dwg.rect((block.position[0] * TEXT_WIDTH + 5,
			block.position[1] * TEXT_HEIGHT + 2.5),
			(findLen(block.text) * TEXT_WIDTH, TEXT_HEIGHT), fill=block.bgColour))
		style = "" if any([
		block.bold, block.italic, block.underline, block.crossedOut]) else None
		if style is not None:
			if block.bold:
				style += "font-weight: bold;"
			if block.italic:
				style += "font-style: italic;"
			if block.underline:
				style += "text-decoration: underline;"
			if block.crossedOut:
				style += "text-decoration: line-through;"
		group.add(dwg.text(block.text, insert=(block.position[0] * TEXT_WIDTH + 5,
		(block.position[1] + 1) * TEXT_HEIGHT), fill=("#" + themeData["base05"]
		if block.fgColour is None else block.fgColour), style=style,
		**{"xml:space": "preserve"} if " " in block.text else {})) # yapf: disable
	dwg.add(group) # type: ignore
	dwg.save() # type: ignore


def ansiToRaster(ansiText: str, fileName: str, theme: Optional[str]=None, wide: bool=True):
	"""convert an ANSI stream to a raster image with pillow

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
	"""
	themeData = safe_load(open(theme if theme is not None else THISDIR + "/onedark.yml"))
	ansiBlocks = AnsiBlocks(ansiText, wide)
	ansiBlocks.process()
	blocks = ansiBlocks.ansiBlocks
	size = (int((95 if wide else 55) * TEXT_WIDTH), int(TEXT_HEIGHT * ansiBlocks.height + 5))
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
	# Iterate through the ANSI blocks
	for block in blocks:
		posY = block.position[1] * TEXT_HEIGHT + 2.5
		if block.bgColour is not None:
			posX = block.position[0] * TEXT_WIDTH + 5
			draw.rectangle((posX, posY, posX + findLen(block.text) * TEXT_WIDTH,
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


def ansiToSVGRaster(ansiText: str, fileName: str, theme: Optional[str]=None, wide: bool=True):
	"""convert an ANSI stream to a raster image using pyppeteer to take a
	screenshot of a generated SVG (hacky but we can get coloured emoji now)

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
	"""
	ansiToSVG(ansiText, THISDIR + "/temp.svg", theme, wide)
	ansiBlocks = AnsiBlocks(ansiText, wide)
	ansiBlocks.process()
	size = (int((95 if wide else 55) * TEXT_WIDTH), int(TEXT_HEIGHT * ansiBlocks.height + 5))
	asyncio.get_event_loop().run_until_complete(
	_doGrabWebpage('file:///' + THISDIR + "/temp.svg", size, fileName))
	try:
		remove(THISDIR + "/temp.svg")
	except PermissionError:
		print("Unable to clean up, manually remove temp.svg from project root " +
		"or ignore")


async def _doGrabWebpage(url: str, resolution: tuple[int, int], fileName: str):
	''' Go to a URL, with a browser with a set resolution and take a screenshot'''
	browser = await launch(
	options={'args': ['--no-sandbox', '--disable-web-security']})
	page = await browser.newPage()
	await page.setViewport({"width": resolution[0], "height": resolution[1]}) # type: ignore
	await page.goto(url) # type: ignore
	await page.screenshot({'path': fileName}) # type: ignore
	await browser.close()


def ansiToHTML(ansiText: str, fileName: str, theme: Optional[str]=None, wide: bool=True):
	"""convert an ANSI stream to a html file

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
	"""
	themeData = safe_load(open(theme if theme is not None else THISDIR + "/onedark.yml"))
	ansiBlocks = AnsiBlocks(ansiText, wide)
	ansiBlocks.process()
	blocks = ansiBlocks.ansiBlocks
	prevY = 0
	html = [
	"<!DOCTYPE html><html style=\"background-color: #" + themeData["base00"] +
	"; font-weight:300; font-size: 14px; font-family: FiraCode NF, Fira Code, Courier New, " +
	"Cousine, monospace;\"><head><title>" + fileName.replace("\\",
	"/").split("/")[-1] + "</title><meta charset=\"utf-8\"/><meta name=\"viewport\" " +
	"content=\"width=device-width, initial-scale=1, shrink-to-fit=no\"><link " +
	"href=\"https://rawcdn.githack.com/tonsky/FiraCode/07666484a9d92ec6ea916b94f776fc2410a87a11/distr/fira_code.css\" "
	+ "rel=\"stylesheet\"></head><body style=\"min-width: " + str(int((95 if wide else 55) * TEXT_WIDTH)) + "px\">"]
	for block in blocks:
		style = "color: " + ("#" + themeData["base05"]
		if block.fgColour is None else block.fgColour) + "; "
		if block.bgColour is not None:
			style += "background-color: " + block.bgColour + "; "
		if block.bold:
			style += "font-weight: bold; "
		if block.italic:
			style += "font-style: italic; "
		if block.underline:
			style += "text-decoration: underline; "
		if block.crossedOut:
			style += "text-decoration: line-through; "
		if block.position[1] > prevY:
			html.append("<br>")
			prevY = block.position[1]
		html.append("<span style=\"{0}\">{1}</span>".format(style[:-1],
		str(escape(block.text)).replace(" ", "&nbsp;")))
	html.append("</body></html>")
	with open(fileName, "w", encoding="utf-8") as file:
		file.write("".join(html))


def ansiToHTMLRaster(ansiText: str, fileName: str, theme: Optional[str]=None, wide: bool=True):
	"""convert an ANSI stream to a raster image using pyppeteer to take a
	screenshot of a generated html (hacky but we can output more like that
	of a terminal now)

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
	"""
	ansiToHTML(ansiText, THISDIR + "/temp.html", theme, wide)
	ansiBlocks = AnsiBlocks(ansiText, wide)
	ansiBlocks.process()
	size = (int((95 if wide else 55) * 8.63) + 16, int(16.8 * ansiBlocks.height + 16))
	asyncio.get_event_loop().run_until_complete(
	_doGrabWebpage('file:///' + THISDIR + "/temp.html", size, fileName))
	try:
		remove(THISDIR + "/temp.html")
	except PermissionError:
		print("Unable to clean up, manually remove temp.html from project root " +
		"or ignore")
