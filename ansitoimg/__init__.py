"""Convert an ANSI string to an image. Great for adding terminal output into a readme.
"""

from __future__ import annotations

import argparse
from sys import exit as sysexit
from sys import stdin, stdout

from ansitoimg.render import (
	ansiToHTML,
	ansiToHTMLRender,
	ansiToRender,
	ansiToSVG,
	ansiToSVGRender,
)
from ansitoimg.utils import TITLE, TEXT_HEIGHT, TEXT_WIDTH, WIDTH_WIDE, _resolveWidth

stdout.reconfigure(encoding="utf-8")


PLUGIN_HELP = "Plugin to use. One of svg, render, svgrender, html, htmlrender, default=svg"


def cli():  # pragma: no cover
	"""Cli entry point."""
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		"input",
		nargs="?",
		help="Filename to read from",
		type=argparse.FileType("r", encoding="utf-8"),
		default=stdin,
	)
	parser.add_argument(
		"output",
		help="Filename to write to",
	)
	parser.add_argument(
		"--plugin",
		"-p",
		help=PLUGIN_HELP,
	)
	parser.add_argument(
		"--theme",
		"-t",
		help="Enter the path to a base24 theme",
	)
	parser.add_argument(
		"--title",
		default=TITLE,
		help="Set a custom title",
	)
	parser.add_argument(
		"--wide",
		"-w",
		action="store_true",
		help="Use a 'wide' virtual terminal (89 chars vs 49)",
	)
	parser.add_argument(
		"--width",
		default=49,
		help="Explicitly set the width in chars",
	)

	args = parser.parse_args()
	ansi = args.input.read()
	width = _resolveWidth(args.wide, args.width)

	# Plugin
	pluginMap = {
		"svg": ansiToSVG,
		"render": ansiToRender,
		"svgrender": ansiToSVGRender,
		"html": ansiToHTML,
		"htmlrender": ansiToHTMLRender,
	}
	if args.plugin is None:
		ansiToSVG(ansi, args.output, args.theme, width=width, title=args.title)
	elif args.plugin in pluginMap:
		pluginMap[args.plugin](ansi, args.output, args.theme, width=width, title=args.title)
	else:
		print(PLUGIN_HELP)
		sysexit(1)
