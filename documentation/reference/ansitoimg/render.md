# Render

[Ansitoimg Index](../README.md#ansitoimg-index) /
[Ansitoimg](./index.md#ansitoimg) /
Render

> Auto-generated documentation for [ansitoimg.render](../../../ansitoimg/render.py) module.

#### Attributes

- `TEXT_HEIGHT` - monospaced chars have a constant height and width: `21`


- [Render](#render)
  - [ansiToHTML](#ansitohtml)
  - [ansiToHTMLRender](#ansitohtmlrender)
  - [ansiToRender](#ansitorender)
  - [ansiToSVG](#ansitosvg)
  - [ansiToSVGRender](#ansitosvgrender)

## ansiToHTML

[Show source in render.py:141](../../../ansitoimg/render.py#L141)

Convert an ANSI stream to a html file.

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image

#### Signature

```python
def ansiToHTML(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = 49,
):
    ...
```



## ansiToHTMLRender

[Show source in render.py:157](../../../ansitoimg/render.py#L157)

Convert an ANSI stream to a Render image using pyppeteer to take a
screenshot of a generated html (hacky but we can output more like that
of a terminal now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image

#### Signature

```python
def ansiToHTMLRender(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = 49,
):
    ...
```



## ansiToRender

[Show source in render.py:85](../../../ansitoimg/render.py#L85)

Convert an ANSI stream to a Render image using pyppeteer to take a
screenshot of a generated SVG (hacky but we can get coloured emoji now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image

#### Signature

```python
def ansiToRender(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = 49,
):
    ...
```



## ansiToSVG

[Show source in render.py:67](../../../ansitoimg/render.py#L67)

Convert an ANSI stream to SVG.

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - file path to SVG to write
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image

#### Signature

```python
def ansiToSVG(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = 49,
):
    ...
```



## ansiToSVGRender

[Show source in render.py:101](../../../ansitoimg/render.py#L101)

Convert an ANSI stream to a Render image using pyppeteer to take a
screenshot of a generated SVG (hacky but we can get coloured emoji now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image

#### Signature

```python
def ansiToSVGRender(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = 49,
):
    ...
```


