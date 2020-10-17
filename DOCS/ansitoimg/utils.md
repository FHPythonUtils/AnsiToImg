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
    - [rgbToHex](#rgbtohex)

## ansi16ToRGB

[[find in source code]](../../ansitoimg/utils.py#L52)

```python
def ansi16ToRGB(
    ansi16: str,
    ansi16Map: Optional[dict[(int, str)]] = None,
    theme: Optional[str] = None,
):
```

convert ANSI 16 to hex rgb

## ansi256ToRGB

[[find in source code]](../../ansitoimg/utils.py#L26)

```python
def ansi256ToRGB(ansi256: str, theme: Optional[str] = None) -> str:
```

convert ANSI 256 to hex rgb

## ansiColourToRGB

[[find in source code]](../../ansitoimg/utils.py#L65)

```python
def ansiColourToRGB(ansiColour: str, theme: Optional[str] = None):
```

convert an ANSI colour to a hex colour

#### Arguments

- `ansiColour` *string* - ANSI colour

#### Returns

- `string` - hex code

## ansiTrueToRgb

[[find in source code]](../../ansitoimg/utils.py#L19)

```python
def ansiTrueToRgb(ansiTrue: str):
```

convert ANSI truecolour to hex rgb

## findLen

[[find in source code]](../../ansitoimg/utils.py#L103)

```python
def findLen(string: list[str]):
```

 find the length of a string and take into account that emojis are double
width

## rgbToHex

[[find in source code]](../../ansitoimg/utils.py#L14)

```python
def rgbToHex(rgb: tuple[(int, int, int)]) -> str:
```

convert rgb tuple to hex
