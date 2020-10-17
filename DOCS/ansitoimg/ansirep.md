# ansirep

> Auto-generated documentation for [ansitoimg.ansirep](../../ansitoimg/ansirep.py) module.

 representation and processing of an ANSI stream into an 'ast' of sorts
such that it can be rendered

- [Ansitoimg](../README.md#ansitoimg-index) / [Modules](../README.md#ansitoimg-modules) / [ansitoimg](index.md#ansitoimg) / ansirep
    - [AnsiBlock](#ansiblock)
    - [AnsiBlocks](#ansiblocks)
        - [AnsiBlocks().process](#ansiblocksprocess)
        - [AnsiBlocks().processCloseSgi](#ansiblocksprocessclosesgi)
        - [AnsiBlocks().processSgi](#ansiblocksprocesssgi)
        - [AnsiBlocks().setAnsiBlocks](#ansiblockssetansiblocks)

## AnsiBlock

[[find in source code]](../../ansitoimg/ansirep.py#L10)

```python
class AnsiBlock():
    def __init__(
        text: str,
        position: tuple[(int, int)],
        bgColour: Optional[str] = None,
        fgColour: Optional[str] = None,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        crossedOut: bool = False,
    ):
```

represent a block of ANSI text. eg [31mhello![0m

ANSI text can have the following attributes:
- text
- background colour
- foreground colour
- absolute char offset
- bold
- italic
- underline
- crossed out

## AnsiBlocks

[[find in source code]](../../ansitoimg/ansirep.py#L48)

```python
class AnsiBlocks():
    def __init__(ansiText: str, wide: bool = True):
```

representation of ANSI blocks

ANSI blocks has the following attributes:
- ANSI text
- ANSI blocks
ANSI blocks also holds a series of attributes that are used when processing
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

### AnsiBlocks().process

[[find in source code]](../../ansitoimg/ansirep.py#L95)

```python
def process():
```

process the ANSI text into a series of ANSI blocks

### AnsiBlocks().processCloseSgi

[[find in source code]](../../ansitoimg/ansirep.py#L172)

```python
def processCloseSgi():
```

 process a closing sgi code and create ANSI blocks accordingly
reset any attributes that need setting

### AnsiBlocks().processSgi

[[find in source code]](../../ansitoimg/ansirep.py#L139)

```python
def processSgi():
```

process an sgi code and set attributes accordingly

### AnsiBlocks().setAnsiBlocks

[[find in source code]](../../ansitoimg/ansirep.py#L114)

```python
def setAnsiBlocks(text: str):
```

create a series of ANSI blocks from the text buffer and other attributes

#### Arguments

- `text` *str* - text from the buffer
