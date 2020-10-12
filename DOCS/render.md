Module ansitoimg.render
=======================
render the ANSI

render as SVG

Functions
---------

    
`ansiToHTML(ansiText: str, fileName: str, theme: Optional[str] = None, wide: bool = True)`
:   convert an ANSI stream to a html file
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
            wide (bool, optional): use a 'wide' terminal 89 vs 49 chars

    
`ansiToHTMLRaster(ansiText: str, fileName: str, theme: Optional[str] = None, wide: bool = True)`
:   convert an ANSI stream to a raster image using pyppeteer to take a
    screenshot of a generated html (hacky but we can output more like that
    of a terminal now)
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
            wide (bool, optional): use a 'wide' terminal 89 vs 49 chars

    
`ansiToRaster(ansiText: str, fileName: str, theme: Optional[str] = None, wide: bool = True)`
:   convert an ANSI stream to a raster image with pillow
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
            wide (bool, optional): use a 'wide' terminal 89 vs 49 chars

    
`ansiToSVG(ansiText: str, fileName: str, theme: Optional[str] = None, wide: bool = True)`
:   convert an ANSI stream to SVG
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): file path to SVG to write
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
            wide (bool, optional): use a 'wide' terminal 89 vs 49 chars

    
`ansiToSVGRaster(ansiText: str, fileName: str, theme: Optional[str] = None, wide: bool = True)`
:   convert an ANSI stream to a raster image using pyppeteer to take a
    screenshot of a generated SVG (hacky but we can get coloured emoji now)
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".
            wide (bool, optional): use a 'wide' terminal 89 vs 49 chars