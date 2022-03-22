# Utils

> Auto-generated documentation for [ansitoimg.utils](../../../ansitoimg/utils.py) module.

Utility functions to get the length of a char and to get the hex colour from an ansi code.

- [Ansitoimg](../README.md#ansitoimg-index) / [Modules](../MODULES.md#ansitoimg-modules) / [Ansitoimg](index.md#ansitoimg) / Utils
    - [ansi16ToRGB](#ansi16torgb)
    - [ansi256ToRGB](#ansi256torgb)
    - [ansiColourToRGB](#ansicolourtorgb)
    - [ansiTrueToRgb](#ansitruetorgb)
    - [findLen](#findlen)
    - [getTheme](#gettheme)
    - [rgbToHex](#rgbtohex)

## ansi16ToRGB

[[find in source code]](../../../ansitoimg/utils.py#L79)

```python
def ansi16ToRGB(
    ansi16: str,
    ansi16Map: dict[int, str] | None = None,
    theme: str | None = None,
):
```

Convert ANSI 16 to hex rgb.

## ansi256ToRGB

[[find in source code]](../../../ansitoimg/utils.py#L39)

```python
def ansi256ToRGB(ansi256: str, theme: str | None = None) -> str:
```

Convert ANSI 256 to hex rgb.

## ansiColourToRGB

[[find in source code]](../../../ansitoimg/utils.py#L109)

```python
def ansiColourToRGB(ansiColour: str, theme: str | None = None):
```

Convert an ANSI colour to a hex colour.

#### Arguments

- `ansiColour` *string* - ANSI colour
- `theme` *Optional[str]* - set a theme (defaults to None.)

#### Returns

- `string` - hex code

## ansiTrueToRgb

[[find in source code]](../../../ansitoimg/utils.py#L27)

```python
def ansiTrueToRgb(ansiTrue: str):
```

Convert ANSI truecolour to hex rgb.

## findLen

[[find in source code]](../../../ansitoimg/utils.py#L148)

```python
def findLen(string: Iterable):
```

Find the length of a string and take into account that emojis are double	width.

## getTheme

[[find in source code]](../../../ansitoimg/utils.py#L13)

```python
def getTheme(theme: str | None) -> dict[str, str]:
```

Get the theme yaml.

## rgbToHex

[[find in source code]](../../../ansitoimg/utils.py#L22)

```python
def rgbToHex(rgb: tuple[int, int, int]) -> str:
```

Convert rgb tuple to hex.
