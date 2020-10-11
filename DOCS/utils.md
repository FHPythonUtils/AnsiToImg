Module ansitoimg.utils
======================
Utility functions to get the length of a char and to get the hex colour from
an ansi code

Functions
---------

    
`ansi16ToRGB(ansi16: str, ansi16Map: Optional[dict[int, str]] = None, theme: Optional[str] = None)`
:   convert ANSI 16 to hex rgb

    
`ansi256ToRGB(ansi256: str, theme: Optional[str] = None) ‑> str`
:   convert ANSI 256 to hex rgb

    
`ansiColourToRGB(ansiColour: str, theme: Optional[str] = None)`
:   convert an ANSI colour to a hex colour
    
    Args:
            ansiColour (string): ANSI colour
    
    Returns:
            string: hex code

    
`ansiTrueToRgb(ansiTrue: str)`
:   convert ANSI truecolour to hex rgb

    
`findLen(string: list[str])`
:   find the length of a string and take into account that emojis are double
    width

    
`rgbToHex(rgb: tuple[int, int, int]) ‑> str`
:   convert rgb tuple to hex