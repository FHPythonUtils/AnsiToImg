Module ansitoimg.render
=======================
render the ANSI

render as SVG

Functions
---------

    
`ansiToHTML(ansiText: str, fileName: str, theme: Optional[str] = None)`
:   convert an ANSI stream to a html file
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".

    
`ansiToHTMLRaster(ansiText: str, fileName: str, theme: Optional[str] = None)`
:   convert an ANSI stream to a raster image using pyppeteer to take a
    screenshot of a generated html (hacky but we can output more like that
    of a terminal now)
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".

    
`ansiToRaster(ansiText: str, fileName: str, theme: Optional[str] = None)`
:   convert an ANSI stream to a raster image with pillow
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".

    
`ansiToSVG(ansiText: str, fileName: str, theme: Optional[str] = None)`
:   convert an ANSI stream to SVG
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): file path to SVG to write
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".

    
`ansiToSVGRaster(ansiText: str, fileName: str, theme: Optional[str] = None)`
:   convert an ANSI stream to a raster image using pyppeteer to take a
    screenshot of a generated SVG (hacky but we can get coloured emoji now)
    
    Args:
            ansiText (str): ANSI text to convert
            fileName (str): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".