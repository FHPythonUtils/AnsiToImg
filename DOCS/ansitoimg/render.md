# render

> Auto-generated documentation for [ansitoimg.render](../../ansitoimg/render.py) module.

Render the ANSI...

- [Ansitoimg](../README.md#ansitoimg-index) / [Modules](../README.md#ansitoimg-modules) / [ansitoimg](index.md#ansitoimg) / render
    - [ansiToHTML](#ansitohtml)
    - [ansiToHTMLRaster](#ansitohtmlraster)
    - [ansiToRaster](#ansitoraster)
    - [ansiToSVG](#ansitosvg)
    - [ansiToSVGRaster](#ansitosvgraster)

#### Attributes

- `TEXT_HEIGHT` - monospaced chars have a constant height and width: `15`

## ansiToHTML

[[find in source code]](../../ansitoimg/render.py#L181)

```python
def ansiToHTML(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
):
```

Convert an ANSI stream to a html file.

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars

## ansiToHTMLRaster

[[find in source code]](../../ansitoimg/render.py#L235)

```python
def ansiToHTMLRaster(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
):
```

Convert an ANSI stream to a raster image using pyppeteer to take a...

screenshot of a generated html (hacky but we can output more like that
of a terminal now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars

## ansiToRaster

[[find in source code]](../../ansitoimg/render.py#L84)

```python
def ansiToRaster(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
):
```

Convert an ANSI stream to a raster image with pillow.

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars

## ansiToSVG

[[find in source code]](../../ansitoimg/render.py#L24)

```python
def ansiToSVG(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
):
```

Convert an ANSI stream to SVG.

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - file path to SVG to write
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars

## ansiToSVGRaster

[[find in source code]](../../ansitoimg/render.py#L147)

```python
def ansiToSVGRaster(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
):
```

Convert an ANSI stream to a raster image using pyppeteer to take a...

screenshot of a generated SVG (hacky but we can get coloured emoji now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
