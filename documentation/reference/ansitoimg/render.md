# Render

[Ansitoimg Index](../README.md#ansitoimg-index) /
[Ansitoimg](./index.md#ansitoimg) /
Render

> Auto-generated documentation for [ansitoimg.render](../../../ansitoimg/render.py) module.

- [Render](#render)
  - [ansiToHTML](#ansitohtml)
  - [ansiToHTMLRender](#ansitohtmlrender)
  - [ansiToRender](#ansitorender)
  - [ansiToSVG](#ansitosvg)
  - [ansiToSVGRender](#ansitosvgrender)

## ansiToHTML

[Show source in render.py:144](../../../ansitoimg/render.py#L144)

Convert an ANSI stream to a html file.

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml"
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Ingored

#### Signature

```python
def ansiToHTML(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    width: int = WIDTH_DEFAULT,
    title: str = TITLE,
): ...
```

#### See also

- [TITLE](./utils.md#title)
- [WIDTH_DEFAULT](./utils.md#width_default)



## ansiToHTMLRender

[Show source in render.py:164](../../../ansitoimg/render.py#L164)

Convert an ANSI stream to a Render image using playwright to take a
screenshot of a generated html (hacky but we can output more like that
of a terminal now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml"
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Ingored

#### Signature

```python
def ansiToHTMLRender(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    width: int = WIDTH_DEFAULT,
    title: str = TITLE,
): ...
```

#### See also

- [TITLE](./utils.md#title)
- [WIDTH_DEFAULT](./utils.md#width_default)



## ansiToRender

[Show source in render.py:81](../../../ansitoimg/render.py#L81)

Convert an ANSI stream to a Render image using playwright to take a
screenshot of a generated SVG (hacky but we can get coloured emoji now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml"
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Defaults to "AnsiToImg (courtesy of Rich)"

#### Signature

```python
def ansiToRender(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    width: int = WIDTH_DEFAULT,
    title: str = TITLE,
): ...
```

#### See also

- [TITLE](./utils.md#title)
- [WIDTH_DEFAULT](./utils.md#width_default)



## ansiToSVG

[Show source in render.py:61](../../../ansitoimg/render.py#L61)

Convert an ANSI stream to SVG.

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - file path to SVG to write
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml"
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Defaults to "AnsiToImg (courtesy of Rich)"

#### Signature

```python
def ansiToSVG(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    width: int = WIDTH_DEFAULT,
    title: str = TITLE,
): ...
```

#### See also

- [TITLE](./utils.md#title)
- [WIDTH_DEFAULT](./utils.md#width_default)



## ansiToSVGRender

[Show source in render.py:101](../../../ansitoimg/render.py#L101)

Convert an ANSI stream to a Render image using playwright to take a
screenshot of a generated SVG (hacky but we can get coloured emoji now)

#### Arguments

- `ansiText` *str* - ANSI text to convert
- `fileName` *str* - image file path
- `theme` *str, optional* - file path to base24 theme to use. Defaults to "onedark.yml"
- `width` *int, optional* - set the width for the image
- `title` *str, optional* - set the title. Defaults to "AnsiToImg (courtesy of Rich)"

#### Signature

```python
def ansiToSVGRender(
    ansiText: str,
    fileName: str,
    theme: str | None = None,
    width: int = WIDTH_DEFAULT,
    title: str = TITLE,
): ...
```

#### See also

- [TITLE](./utils.md#title)
- [WIDTH_DEFAULT](./utils.md#width_default)
