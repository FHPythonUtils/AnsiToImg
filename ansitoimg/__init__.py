"""Convert an ANSI string to an image. Great for adding terminal output into a readme."""

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
from ansitoimg.utils import TITLE, WIDTH_DEFAULT, WIDTH_WIDE

stdout.reconfigure(encoding="utf-8")


PLUGIN_HELP = "Plugin to use. One of svg, render, svgrender, html, htmlrender, default=svg"


def cli() -> None:  # pragma: no cover
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
		help=f"Use a 'wide' virtual terminal ({WIDTH_WIDE} chars vs {WIDTH_DEFAULT})",
	)
	parser.add_argument(
		"--width",
		default=WIDTH_DEFAULT,
		type=int,
		help="Explicitly set the width in chars, use 'auto' to attempt to automatically "
		"calculate this from your environment",
	)

	args = parser.parse_args()
	ansi = args.input.read()

	width = args.width
	if width == WIDTH_DEFAULT and args.wide:
		width = WIDTH_WIDE

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
