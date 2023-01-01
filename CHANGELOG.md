# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2022.2 - 2022/069/02

- Add custom width by passing `width` to render functions. Thanks https://github.com/punctuations
  	(https://github.com/FHPythonUtils/AnsiToImg/issues/4)

	eg.

	```py
	ansiToSVG(cat, f"{THISDIR}/data/cat.svg", width=100)
	```

## 2022.1 - 2022/06/19

- Use rich to do the heavy lifting (see https://github.com/FHPythonUtils/AnsiToImg/issues/3)

## 2022 - 2022/01/24

- Bump pillow version (CVE-2022-22815, CVE-2022-22816, CVE-2022-22817)
- Update deps
- Rename Raster functions to Render
- Add formal tests

## 2021.0.4 - 2021/11/11

- update deps
- add pre-commit
- use f-strings
- improve pyproject.toml
- reformat *.md

## 2021.0.3 - 2021/09/13

- Update pillow

## 2021.0.2 - 2021/06/04

- pyupgrade
- reformatted code
- update pyproject

## 2021.0.1 - 2021/03/18

- Update Pillow >= 8.1.1 due to high severity security vulnerabilities:
	- CVE-2021-27923
	- CVE-2020-35654
	- CVE-2020-35653
	- CVE-2021-27921
	- CVE-2021-27922
	- CVE-2020-35655

## 2021 - 2021/01/24

- Fix unclosed file warnings

## 2020.4.4 - 2020/11/09

- Optimize svg file size by omitting xml:space: preserve on elements without spaces
- Use font-weight 300

## 2020.4.2 - 2020/10/17

- Update dependencies

## 2020.4.1 - 2020/10/12

- Add 'wide' parameter to renderers (enabled by default)
	- true: width of 89, false: width of 49
- Run from the command line with `ansitoimg`
- set stdout to utf-8

## 2020.4 - 2020/10/11

- Added typing (so dropping python < 3.7)
- Support sgi chars in the form ESC[0Xm - fixing quite a lot of bugs
- Excess spaces are now rendered in svg and html

## 2020.3.3 - 2020/06/07

- scale html better to mobile
- add min width of 70 chars for html
- Change default theme value to None and check for none when reading theme file

## 2020.3.2 - 2020/06/06

- use google fonts for Fira Code in html if not present

## 2020.3.1 - 2020/06/06

- bugfix bgColour sizes for ansiToSVG and ansiToRaster

## 2020.3 - 2020/06/06

- added ansiToHTML
- added ansiToHTMLRaster

## 2020.2 - 2020/06/05

- added ansiToSVGRaster

## 2020.1 - 2020/06/05

- added ansiToRaster

## 2020 - 2020/06/05

- First release
