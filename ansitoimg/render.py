"""Render the ANSI
"""
from __future__ import annotations

import asyncio
import re
from io import StringIO
from os import remove
from pathlib import Path

from pyppeteer import launch
from rich import text
from rich.console import Console
from rich.terminal_theme import TerminalTheme
from yaml import safe_load

THISDIR = str(Path(__file__).resolve().parent)

# monospaced chars have a constant height and width
TEXT_HEIGHT = 21
TEXT_WIDTH = 12


def _doRichRender(ansiText: str, wide: bool = True, width: int = 49) -> Console:
	dynamicWidth = round(width * 1.82) if wide else width

	console = Console(width=dynamicWidth, record=True, file=StringIO())
	richText = text.Text.from_ansi(ansiText)
	console.print(richText)
	console.height = len(richText.wrap(console, width=round(width * 1.82) if wide else width))
	return console


def _doRichTerminalTheme(theme: str | None) -> TerminalTheme:
	base24 = safe_load(Path(theme or f"{THISDIR}/onedark.yml").read_text(encoding="utf-8"))

	return TerminalTheme(
		background=_hexToRGB(base24["base00"]),
		foreground=_hexToRGB(base24["base05"]),
		normal=[
			_hexToRGB(base24["base01"]),
			_hexToRGB(base24["base08"]),
			_hexToRGB(base24["base0B"]),
			_hexToRGB(base24["base09"]),
			_hexToRGB(base24["base0D"]),
			_hexToRGB(base24["base0E"]),
			_hexToRGB(base24["base0C"]),
			_hexToRGB(base24["base06"]),
		],
		bright=[
			_hexToRGB(base24["base02"]),
			_hexToRGB(base24["base12"]),
			_hexToRGB(base24["base14"]),
			_hexToRGB(base24["base13"]),
			_hexToRGB(base24["base16"]),
			_hexToRGB(base24["base17"]),
			_hexToRGB(base24["base15"]),
			_hexToRGB(base24["base07"]),
		],
	)


def _hexToRGB(colourCode: str) -> tuple[int, int, int]:
	return tuple(int(colourCode[i : i + 2], base=16) for i in (0, 2, 4))


def ansiToSVG(
	ansiText: str, fileName: str, theme: str | None = None, wide: bool = True, width: int = 49
):
	"""Convert an ANSI stream to SVG.

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): file path to SVG to write
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
		width (int, optional): set the width for the image
	"""
	console = _doRichRender(ansiText, wide, width)
	console.save_svg(
		fileName, theme=_doRichTerminalTheme(theme), title="AnsiToImg (courtesy of Rich)"
	)


def ansiToRender(
	ansiText: str, fileName: str, theme: str | None = None, wide: bool = True, width: int = 49
):
	"""Convert an ANSI stream to a Render image using pyppeteer to take a
	screenshot of a generated SVG (hacky but we can get coloured emoji now)

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
		width (int, optional): set the width for the image
	"""
	return ansiToSVGRender(ansiText, fileName, theme, wide, width)


def ansiToSVGRender(
	ansiText: str, fileName: str, theme: str | None = None, wide: bool = True, width: int = 49
):
	"""Convert an ANSI stream to a Render image using pyppeteer to take a
	screenshot of a generated SVG (hacky but we can get coloured emoji now)

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
		width (int, optional): set the width for the image
	"""
	console = _doRichRender(ansiText, wide, width)
	tempFileName = f"{THISDIR}/temp.svg"
	ansiToSVG(ansiText, tempFileName, theme, wide, width)
	match = re.search(
		r'^<svg.*?viewBox="[\d.]+ [\d.]+ ([\d.]+) ([\d.]+)',
		Path(tempFileName).read_text(encoding="utf-8"),
	)
	size = (console.width * TEXT_WIDTH, (console.height + 2) * TEXT_HEIGHT)
	if match:
		size = (int(float(match.group(1))), int(float(match.group(2))))
	asyncio.run(_doGrabWebpage(f"file:///{tempFileName}", size, fileName))
	try:
		remove(tempFileName)
	except PermissionError:
		print("Unable to clean up, manually remove temp.svg from project root or ignore")


async def _doGrabWebpage(url: str, resolution: tuple[int, int], fileName: str):
	"""Go to a URL, with a browser with a set resolution and take a screenshot."""
	browser = await launch(options={"args": ["--no-sandbox", "--disable-web-security"]})
	page = await browser.newPage()
	await page.setViewport({"width": resolution[0], "height": resolution[1]})  # type: ignore
	await page.goto(url)  # type: ignore
	await page.screenshot({"path": fileName, "omitBackground": True})  # type: ignore
	await browser.close()


def ansiToHTML(
	ansiText: str, fileName: str, theme: str | None = None, wide: bool = True, width: int = 49
):
	"""Convert an ANSI stream to a html file.

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
		width (int, optional): set the width for the image
	"""
	console = _doRichRender(ansiText, wide, width)
	console.save_html(fileName, theme=_doRichTerminalTheme(theme))


def ansiToHTMLRender(
	ansiText: str, fileName: str, theme: str | None = None, wide: bool = True, width: int = 49
):
	"""Convert an ANSI stream to a Render image using pyppeteer to take a
	screenshot of a generated html (hacky but we can output more like that
	of a terminal now)

	Args:
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
		wide (bool, optional): use a 'wide' terminal 89 vs 49 chars
		width (int, optional): set the width for the image
	"""
	console = _doRichRender(ansiText, wide, width)
	ansiToHTML(ansiText, f"{THISDIR}/temp.html", theme, wide, width)
	size = (console.width * TEXT_WIDTH, (console.height + 1) * TEXT_HEIGHT)
	asyncio.run(_doGrabWebpage(f"file:///{THISDIR}/temp.html", size, fileName))
	try:
		remove(f"{THISDIR}/temp.html")
	except PermissionError:
		print("Unable to clean up, manually remove temp.html from project root or ignore")
