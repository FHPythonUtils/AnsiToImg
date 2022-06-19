""" tests """
from __future__ import annotations

import sys
from pathlib import Path

import imgcompare

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from ansitoimg.render import ansiToHTMLRender, ansiToRender, ansiToSVGRender

fredHappyfaceHD = Path(f"{THISDIR}/data/fredHappyfaceHD.txt").read_text(encoding="utf-8")


def test_html_render():
	output = f"{THISDIR}/data/fredHappyfaceHD.html.png"
	ansiToHTMLRender(fredHappyfaceHD, output)
	imgcompare.is_equal(output, f"{THISDIR}/data/fredHappyfaceHD.html_expected.png", tolerance=0.2)


def test_render():
	output = f"{THISDIR}/data/fredHappyfaceHD.png"
	ansiToRender(fredHappyfaceHD, output)
	imgcompare.is_equal(output, f"{THISDIR}/data/fredHappyfaceHD_expected.png", tolerance=0.2)


def test_svg_render():
	output = f"{THISDIR}/data/fredHappyfaceHD.svg.png"
	ansiToSVGRender(fredHappyfaceHD, output)
	imgcompare.is_equal(output, f"{THISDIR}/data/fredHappyfaceHD.svg_expected.png", tolerance=0.2)
