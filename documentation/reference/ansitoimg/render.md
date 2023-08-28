# Render

> Auto-generated documentation for [ansitoimg.render](../../../ansitoimg/render.py) module.

- [Ansitoimg](../README.md#ansitoimg-index) / [Modules](../MODULES.md#ansitoimg-modules) / [Ansitoimg](index.md#ansitoimg) / Render
    - [ansiToHTML](#ansitohtml)
    - [ansiToHTMLRender](#ansitohtmlrender)
    - [ansiToRender](#ansitorender)
    - [ansiToSVG](#ansitosvg)
    - [ansiToSVGRender](#ansitosvgrender)

## ansiToHTML

[[find in source code]](../../../ansitoimg/render.py#L150)

```python
def ansiToHTML(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = WIDTH_DEFAULT,
    title: str = TITLE,
):
```

Convert an ANSI stream to a html file.

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Ingored

#### See also

- [TITLE](utils.md#title)
- [WIDTH_DEFAULT](utils.md#width_default)

## ansiToHTMLRender

[[find in source code]](../../../ansitoimg/render.py#L172)

```python
def ansiToHTMLRender(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = WIDTH_DEFAULT,
):
```

Convert an ANSI stream to a Render image using pyppeteer to take a
screenshot of a generated html (hacky but we can output more like that
of a terminal now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Ingored

#### See also

- [WIDTH_DEFAULT](utils.md#width_default)

## ansiToRender

[[find in source code]](../../../ansitoimg/render.py#L83)

```python
def ansiToRender(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = WIDTH_DEFAULT,
    title: str = TITLE,
):
```

Convert an ANSI stream to a Render image using pyppeteer to take a
screenshot of a generated SVG (hacky but we can get coloured emoji now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Defaults to "AnsiToImg (courtesy of Rich)"

#### See also

- [TITLE](utils.md#title)
- [WIDTH_DEFAULT](utils.md#width_default)

## ansiToSVG

[[find in source code]](../../../ansitoimg/render.py#L61)

```python
def ansiToSVG(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = WIDTH_DEFAULT,
    title: str = TITLE,
):
```

Convert an ANSI stream to SVG.

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - file path to SVG to write
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Defaults to "AnsiToImg (courtesy of Rich)"

#### See also

- [TITLE](utils.md#title)
- [WIDTH_DEFAULT](utils.md#width_default)

## ansiToSVGRender

[[find in source code]](../../../ansitoimg/render.py#L105)

```python
def ansiToSVGRender(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    wide: bool = True,
    width: int = WIDTH_DEFAULT,
    title: str = TITLE,
):
```

Convert an ANSI stream to a Render image using pyppeteer to take a
screenshot of a generated SVG (hacky but we can get coloured emoji now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml".
- `wide` *bool, optional* - use a 'wide' terminal 89 vs 49 chars
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Defaults to "AnsiToImg (courtesy of Rich)"

#### See also

- [TITLE](utils.md#title)
- [WIDTH_DEFAULT](utils.md#width_default)
