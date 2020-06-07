Module ansitoimg.render
=======================
render the ANSI

render as SVG

Functions
---------

    
`ansiToHTML(ansiText, fileName, theme=None)`
:   convert an ANSI stream to a html file
    
    Args:
            ansiText (string): ANSI text to convert
            fileName (string): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".

    
`ansiToHTMLRaster(ansiText, fileName, theme=None)`
:   convert an ANSI stream to a raster image using pyppeteer to take a
    screenshot of a generated html (hacky but we can output more like that
    of a terminal now)
    
    Args:
            ansiText (string): ANSI text to convert
            fileName (string): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".

    
`ansiToRaster(ansiText, fileName, theme=None)`
:   convert an ANSI stream to a raster image with pillow
    
    Args:
            ansiText (string): ANSI text to convert
            fileName (string): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".

    
`ansiToSVG(ansiText, fileName, theme=None)`
:   convert an ANSI stream to SVG
    
    Args:
            ansiText (string): ANSI text to convert
            fileName (string): file path to SVG to write
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".

    
`ansiToSVGRaster(ansiText, fileName, theme=None)`
:   convert an ANSI stream to a raster image using pyppeteer to take a
    screenshot of a generated SVG (hacky but we can get coloured emoji now)
    
    Args:
            ansiText (string): ANSI text to convert
            fileName (string): image file path
            theme (str, optional): file path to base24 theme to use. Defaults to "onedark.yml".