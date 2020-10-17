# Changelog
All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

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
