[![Github top language](https://img.shields.io/github/languages/top/FHPythonUtils/AnsiToImg.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[proj].svg?style=for-the-badge)](https://www.codacy.com/gh/FHPythonUtils/AnsiToImg)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/AnsiToImg.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/AnsiToImg.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/AnsiToImg.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/AnsiToImg.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/AnsiToImg.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/ansitoimg.svg?style=for-the-badge)](https://pypi.org/project/ansitoimg/)
[![PyPI Version](https://img.shields.io/pypi/v/ansitoimg.svg?style=for-the-badge)](https://pypi.org/project/ansitoimg/)

<!-- omit in toc -->
# AnsiToImg

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Convert an ansi string to an image. Great for adding terminal output into a readme.

- [Examples](#examples)
	- [SVG Image](#svg-image)
	- [Raster Image](#raster-image)
	- [Windows Terminal](#windows-terminal)
- [Choosing ansiToSVG or ansiToRaster](#choosing-ansitosvg-or-ansitoraster)
	- [ansiToSVG](#ansitosvg)
	- [ansiToRaster](#ansitoraster)
- [Changelog](#changelog)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [How to update, build and publish](#how-to-update-build-and-publish)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog-1)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)

## Examples

Here is an example of some code and the images it produces:

```python
import sys
import os
from pathlib import Path
import platform
import ctypes
from catimage.catimage import generateHDColour

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from ansitoimg.txtrender import ansiToSVG, ansiToRaster


if platform.system() == "Windows":
	kernel32 = ctypes.windll.kernel32
	kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

example = "👋\033[32mHello\033[0m, \033[34mWorld\033[0m🌏\033[31m!\033[0m\n\033[41m👋\033[0m\033[43m🦄\033[0m\033[42m🐘\033[0m\033[3m\033[9m13\033[0m\033[1m3\033[0m\033[4m7\033[0m\033[46m🍄\033[0m\033[44m🎃\033[0m\033[45m🐦\033[0m"
ansiToSVG(example, THISDIR + "/example.svg")
ansiToRaster(example, THISDIR + "/example.png")

example2 = "hello\nworld\n\033[42m\033[31mwe meet again\033[0m\nABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗😙😚☺🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪asdfghjk"
ansiToSVG(example2, THISDIR + "/example2.svg")
ansiToRaster(example, THISDIR + "/example.png")

example3 = generateHDColour(THISDIR + "/test.png", 40)
ansiToSVG(example3, THISDIR + "/example3.svg")
ansiToRaster(example, THISDIR + "/example.png")
```

### SVG Image
![example](test/example.svg)

![example2](test/example2.svg)

![example3](test/example3.svg)

### Raster Image
![example](test/example.png)

![example2](test/example2.png)

![example3](test/example3.png)


### Windows Terminal

![winterm](readme-assets/terminal.png)

## Choosing ansiToSVG or ansiToRaster

### ansiToSVG
This is better for the vast majority of cases as the image sizes are smaller
for reasonably simple ansi sequences. The image size scales proportionally
with the length of the ansi sequence. A large number of applications tend to
opt for shorter sequences for output making `ansiToSVG` the better option.
`ansiToSVG` also handles emoji as well as the OS does. For instance, on Windows
10 one can expect full colour emoji. Image sizes can get out of hand for some
cases such as catimage output as those tend to be very long ansi sequences.

### ansiToRaster
The image size does not scale to the length of the ansi sequence but does scale
to the number of lines of terminal output. This is ideal for output of complex
ansi sequences that would be huge if `ansiToSVG` were used. However, emojis are
in black and white and show quite poorly on coloured backgrounds.

## Changelog
See the [CHANGELOG](/CHANGELOG.md) for more information.

## Install With PIP

```python
pip install ansitoimg
```

Head to https://pypi.org/project/ansitoimg/ for more info

## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.8
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## How to update, build and publish

1. Ensure you have installed the following dependencies
	Linux
	```bash
	wget dephell.org/install | python3.8
	wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.8
	```
	Windows
	```powershell
	(wget dephell.org/install -UseBasicParsing).Content | python
	(wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
	```
2. Use poetry for the heavy lifting and dephell to generate requirements
	```bash
	poetry update
	dephell deps convert
	```
3. Build/ Publish
	```bash
	poetry build
	poetry publish
	```
	or
	```bash
	poetry publish --build
	```
## Community Files
### Licence
MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md) for more information.

### Support
Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the [Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md) for more information.
