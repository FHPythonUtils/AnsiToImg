"""Convert an ANSI string to an image. Great for adding terminal output into a readme.
"""

import argparse
from sys import exit as sysexit, stdin, stdout

stdout.reconfigure(encoding="utf-8")


from ansitoimg.render import (ansiToHTML, ansiToHTMLRaster, ansiToRaster,
                              ansiToSVG, ansiToSVGRaster)

PLUGIN_HELP = "Plugin to use. One of svg, raster, svgraster, html, htmlraster, default=svg"


def cli():
	"""Cli entry point."""
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		"input",
		nargs="?",
		help="Filename to read from",
		type=argparse.FileType("r", encoding="utf-8"),
		default=stdin,
	)
	parser.add_argument("output", help="Filename to write to")
	parser.add_argument("--plugin", "-p", help=PLUGIN_HELP)
	parser.add_argument("--theme", "-t", help="Enter the path to a base24 theme")
	parser.add_argument(
		"--wide", "-w", action="store_true", help="Use a 'wide' virtual terminal (89 chars vs 49)"
	)

	args = parser.parse_args()

	ansi = args.input.read()

	# Plugin
	pluginMap = {
		"svg": ansiToSVG,
		"raster": ansiToRaster,
		"svgraster": ansiToSVGRaster,
		"html": ansiToHTML,
		"htmlraster": ansiToHTMLRaster,
	}
	if args.plugin is None:
		ansiToSVG(ansi, args.output, args.theme, args.wide)
	elif args.plugin in pluginMap:
		pluginMap[args.plugin](ansi, args.output, args.theme, args.wide)
	else:
		print(PLUGIN_HELP)
		sysexit(1)
