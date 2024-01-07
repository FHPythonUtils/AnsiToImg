""" tests """
from __future__ import annotations

import sys
from pathlib import Path

import imgcompare

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from ansitoimg.render import ansiToHTML, ansiToHTMLRender, ansiToRender, ansiToSVGRender
from ansitoimg.utils import WIDTH_WIDE

fredHappyfaceHD = Path(f"{THISDIR}/data/fredHappyfaceHD.txt").read_text(encoding="utf-8")
fancyHelloWorld = Path(f"{THISDIR}/data/fancyHelloWorld.txt").read_text(encoding="utf-8")


def test_html():
	output = f"{THISDIR}/data/fredHappyfaceHD.html"
	expected = f"{THISDIR}/data/fredHappyfaceHD_expected.html"
	ansiToHTML(fredHappyfaceHD, output, width=WIDTH_WIDE)
	assert Path(output).read_text(encoding="utf-8") == Path(expected).read_text(encoding="utf-8")


def util_svg_render(slug: str, file=fredHappyfaceHD, **kwargs):
	output = f"{THISDIR}/data/{slug}.svg.png"
	ansiToSVGRender(file, output, **kwargs)
	imgcompare.is_equal(output, f"{THISDIR}/data/{slug}.svg_expected.png", tolerance=0.2)


def test_html_render():
	output = f"{THISDIR}/data/fredHappyfaceHD.html.png"
	ansiToHTMLRender(fredHappyfaceHD, output, width=WIDTH_WIDE)
	imgcompare.is_equal(output, f"{THISDIR}/data/fredHappyfaceHD.html_expected.png", tolerance=0.2)


def test_render():
	output = f"{THISDIR}/data/fredHappyfaceHD.png"
	ansiToRender(fredHappyfaceHD, output, width=WIDTH_WIDE)
	imgcompare.is_equal(output, f"{THISDIR}/data/fredHappyfaceHD_expected.png", tolerance=0.2)


def test_svg_render():
	util_svg_render("fredHappyfaceHD", width=WIDTH_WIDE)


def test_svg_hw20():
	util_svg_render("hw20", fancyHelloWorld, width=20)


def test_svg_hw40test():
	util_svg_render("hw40test", fancyHelloWorld, width=40, title="test")
