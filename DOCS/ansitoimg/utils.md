# utils

> Auto-generated documentation for [ansitoimg.utils](../../ansitoimg/utils.py) module.

Utility functions to get the length of a char and to get the hex colour from
an ansi code

- [Ansitoimg](../README.md#ansitoimg-index) / [Modules](../README.md#ansitoimg-modules) / [ansitoimg](index.md#ansitoimg) / utils
    - [ansi16ToRGB](#ansi16torgb)
    - [ansi256ToRGB](#ansi256torgb)
    - [ansiColourToRGB](#ansicolourtorgb)
    - [ansiTrueToRgb](#ansitruetorgb)
    - [findLen](#findlen)
    - [getTheme](#gettheme)
    - [rgbToHex](#rgbtohex)

## ansi16ToRGB

[[find in source code]](../../ansitoimg/utils.py#L57)

```python
def ansi16ToRGB(
    ansi16: str,
    ansi16Map: Optional[dict[(int, str)]] = None,
    theme: Optional[str] = None,
):
```

convert ANSI 16 to hex rgb

## ansi256ToRGB

[[find in source code]](../../ansitoimg/utils.py#L31)

```python
def ansi256ToRGB(ansi256: str, theme: Optional[str] = None) -> str:
```

convert ANSI 256 to hex rgb

## ansiColourToRGB

[[find in source code]](../../ansitoimg/utils.py#L70)

```python
def ansiColourToRGB(ansiColour: str, theme: Optional[str] = None):
```

convert an ANSI colour to a hex colour

#### Arguments

- `ansiColour` *string* - ANSI colour

#### Returns

- `string` - hex code

## ansiTrueToRgb

[[find in source code]](../../ansitoimg/utils.py#L24)

```python
def ansiTrueToRgb(ansiTrue: str):
```

convert ANSI truecolour to hex rgb

## findLen

[[find in source code]](../../ansitoimg/utils.py#L108)

```python
def findLen(string: str):
```

 find the length of a string and take into account that emojis are double
width

## getTheme

[[find in source code]](../../ansitoimg/utils.py#L13)

```python
def getTheme(theme: str):
```

get the theme yaml

## rgbToHex

[[find in source code]](../../ansitoimg/utils.py#L19)

```python
def rgbToHex(rgb: tuple[(int, int, int)]) -> str:
```

convert rgb tuple to hex
