from __future__ import annotations

import re
import tempfile
from io import StringIO
from pathlib import Path

from install_playwright import install
from playwright.sync_api import sync_playwright
from rich import text
from rich.console import Console
from rich.terminal_theme import TerminalTheme
from yaml import safe_load

from ansitoimg.utils import TEXT_HEIGHT, TEXT_WIDTH, TITLE, WIDTH_DEFAULT

THISDIR = str(Path(__file__).resolve().parent)


def _doRichRender(ansiText: str, width: int = WIDTH_DEFAULT) -> Console:
	console = Console(width=width, record=True, file=StringIO())
	richText = text.Text.from_ansi(ansiText)
	console.print(richText)
	console.height = len(richText.wrap(console, width=width))
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
	ansiText: str,
	fileName: str,
	theme: str | None = None,
	width: int = WIDTH_DEFAULT,
	title: str = TITLE,
) -> None:
	"""Convert an ANSI stream to SVG.

	Args:
	----
		ansiText (str): ANSI text to convert
		fileName (str): file path to SVG to write
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml"
		width (int, optional): set the width for the image
		title (str, optional): set the title. Defaults to "AnsiToImg (courtesy of Rich)"

	"""
	console = _doRichRender(ansiText, width)
	console.save_svg(fileName, theme=_doRichTerminalTheme(theme), title=title)


def ansiToRender(
	ansiText: str,
	fileName: str,
	theme: str | None = None,
	width: int = WIDTH_DEFAULT,
	title: str = TITLE,
) -> None:
	"""Convert an ANSI stream to a Render image using playwright to take a
	screenshot of a generated SVG (hacky but we can get coloured emoji now).

	Args:
	----
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml"
		width (int, optional): set the width for the image
		title (str, optional): set the title. Defaults to "AnsiToImg (courtesy of Rich)"

	"""
	return ansiToSVGRender(ansiText, fileName, theme, width, title)


def ansiToSVGRender(
	ansiText: str,
	fileName: str,
	theme: str | None = None,
	width: int = WIDTH_DEFAULT,
	title: str = TITLE,
) -> None:
	"""Convert an ANSI stream to a Render image using playwright to take a
	screenshot of a generated SVG (hacky but we can get coloured emoji now).

	Args:
	----
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml"
		width (int, optional): set the width for the image
		title (str, optional): set the title. Defaults to "AnsiToImg (courtesy of Rich)"

	"""
	console = _doRichRender(ansiText, width)
	tempFileName = tempfile.mktemp(suffix=".svg")
	ansiToSVG(ansiText, tempFileName, theme, width, title)
	match = re.search(
		r'^<svg.*?viewBox="[\d.]+ [\d.]+ ([\d.]+) ([\d.]+)',
		Path(tempFileName).read_text(encoding="utf-8"),
	)
	size = (console.width * TEXT_WIDTH, (console.height + 2) * TEXT_HEIGHT)
	if match:
		size = (int(float(match.group(1))), int(float(match.group(2))))
	_doGrabWebpage(f"file:///{tempFileName}", size, fileName)
	Path(tempFileName).unlink()


def _doGrabWebpage(url: str, resolution: tuple[int, int], fileName: str) -> None:
	"""Go to a URL, with a browser with a set resolution and take a screenshot."""
	with sync_playwright() as p:
		install(p.chromium)
		browser = p.chromium.launch()
		page = browser.new_page()
		page.set_viewport_size({"width": resolution[0], "height": resolution[1]})
		page.goto(url)
		page.screenshot(path=fileName, omit_background=True)
		browser.close()


def ansiToHTML(
	ansiText: str,
	fileName: str,
	theme: str | None = None,
	width: int = WIDTH_DEFAULT,
	title: str = TITLE,
) -> None:
	"""Convert an ANSI stream to a html file.

	Args:
	----
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml"
		width (int, optional): set the width for the image
		title (str, optional): set the title. Ingored

	"""
	console = _doRichRender(ansiText, width)
	console.save_html(fileName, theme=_doRichTerminalTheme(theme))


def ansiToHTMLRender(
	ansiText: str,
	fileName: str,
	theme: str | None = None,
	width: int = WIDTH_DEFAULT,
	title: str = TITLE,
) -> None:
	"""Convert an ANSI stream to a Render image using playwright to take a
	screenshot of a generated html (hacky but we can output more like that
	of a terminal now).

	Args:
	----
		ansiText (str): ANSI text to convert
		fileName (str): image file path
		theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml"
		width (int, optional): set the width for the image
		title (str, optional): set the title. Ingored

	"""
	console = _doRichRender(ansiText, width)
	tempFileName = tempfile.mktemp(suffix=".html")
	ansiToHTML(ansiText, tempFileName, theme, width)
	size = (console.width * TEXT_WIDTH, (console.height + 1) * TEXT_HEIGHT)
	_doGrabWebpage(f"file:///{tempFileName}", size, fileName)
	Path(tempFileName).unlink()
