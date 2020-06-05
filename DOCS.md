<a name=".ansitoimg"></a>
## ansitoimg

<a name=".ansitoimg.ansire"></a>
## ansitoimg.ansire

representation and processing of an ansi stream into an 'ast' of sorts
such that it can be rendered

<a name=".ansitoimg.ansire.AnsiBlock"></a>
### AnsiBlock

```python
class AnsiBlock()
```

represent a block of ansi text. eg \033[31mhello!\033[0m

ansi text can have the following attributes:
- text
- background colour
- foreground colour
- absolute char offset
- bold
- italic
- underline
- crossed out

<a name=".ansitoimg.ansire.AnsiBlock.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(text, position, bgColour=None, fgColour=None, bold=False, italic=False, underline=False, crossedOut=False)
```

Constructor

**Arguments**:

- `text` _string_ - text content to render
- `position` _int, int_ - x, y tuple to store the absolute offset in chars
- `bgColour` _string, optional_ - background colour. Defaults to None.
- `fgColour` _string, optional_ - foreground colour. Defaults to None.
- `bold` _bool, optional_ - is text bold?. Defaults to False.
- `italic` _bool, optional_ - is text italic?. Defaults to False.
- `underline` _bool, optional_ - is text underlined?. Defaults to False.
- `crossedOut` _bool, optional_ - is text crossed out?. Defaults to False.

<a name=".ansitoimg.ansire.AnsiBlocks"></a>
### AnsiBlocks

```python
class AnsiBlocks()
```

representation of ansi blocks

ansi blocks has the following attributes:
- ansi text
- ansi blocks
ansi blocks also holds a series of attributes that are used when processing
- sgi buffer
- text buffer
- background colour
- foreground colour
- absolute char offset
- bold
- italic
- underline
- crossed out
- height
- char pointer

<a name=".ansitoimg.ansire.AnsiBlocks.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(ansiText)
```

Constructor

**Arguments**:

- `ansiText` _string_ - ansi text stream to process

<a name=".ansitoimg.ansire.AnsiBlocks.process"></a>
#### process

```python
 | process()
```

process the ansi text into a series of ansi blocks

<a name=".ansitoimg.ansire.AnsiBlocks.setAnsiBlocks"></a>
#### setAnsiBlocks

```python
 | setAnsiBlocks(text)
```

create a series of ansi blocks from the text buffer and other attributes

**Arguments**:

- `text` _string_ - text from the buffer

<a name=".ansitoimg.ansire.AnsiBlocks.processSgi"></a>
#### processSgi

```python
 | processSgi()
```

process an sgi code and set attributes accordingly

<a name=".ansitoimg.ansire.AnsiBlocks.processCloseSgi"></a>
#### processCloseSgi

```python
 | processCloseSgi()
```

process a closing sgi code and create ansi blocks accordingly
reset any attributes that need setting

<a name=".ansitoimg.render"></a>
## ansitoimg.render

render the ansi

render as svg

<a name=".ansitoimg.render.ansiToSVG"></a>
#### ansiToSVG

```python
ansiToSVG(ansiText, fileName, theme=THISDIR + "/onedark.yml")
```

convert an ansi stream to svg

**Arguments**:

- `ansiText` _string_ - ansi text to convert
- `fileName` _string_ - file path to svg to write
- `theme` _str, optional_ - file path to theme to use. Defaults to "onedark.yml".

<a name=".ansitoimg.utils"></a>
## ansitoimg.utils

use svg write for much of this

as per terminal environment

<a name=".ansitoimg.utils.rgbToHex"></a>
#### rgbToHex

```python
rgbToHex(rgb)
```

convert rgb tuple to hex

<a name=".ansitoimg.utils.ansiTrueToRgb"></a>
#### ansiTrueToRgb

```python
ansiTrueToRgb(ansiTrue)
```

convert ansi truecolour to hex rgb

<a name=".ansitoimg.utils.ansi256ToRGB"></a>
#### ansi256ToRGB

```python
ansi256ToRGB(ansi256, theme=THISDIR + "/onedark.yml")
```

convert ansi 256 to hex rgb

<a name=".ansitoimg.utils.ansi16ToRGB"></a>
#### ansi16ToRGB

```python
ansi16ToRGB(ansi16, ansi16Map=None, theme=THISDIR + "/onedark.yml")
```

convert ansi 16 to hex rgb

<a name=".ansitoimg.utils.ansiColourToRGB"></a>
#### ansiColourToRGB

```python
ansiColourToRGB(ansiColour, theme=THISDIR + "/onedark.yml")
```

convert an ansi colour to a hex colour

**Arguments**:

- `ansiColour` _string_ - ansi colour
  

**Returns**:

- `string` - hex code

<a name=".ansitoimg.utils.findLen"></a>
#### findLen

```python
findLen(string)
```

find the length of a string and take into account that emojis are double
width

