Module ansitoimg.utils
======================
use SVG write for much of this

as per terminal environment

Functions
---------

    
`ansi16ToRGB(ansi16, ansi16Map=None, theme=None)`
:   convert ANSI 16 to hex rgb

    
`ansi256ToRGB(ansi256, theme=None)`
:   convert ANSI 256 to hex rgb

    
`ansiColourToRGB(ansiColour, theme=None)`
:   convert an ANSI colour to a hex colour
    
    Args:
            ansiColour (string): ANSI colour
    
    Returns:
            string: hex code

    
`ansiTrueToRgb(ansiTrue)`
:   convert ANSI truecolour to hex rgb

    
`findLen(string)`
:   find the length of a string and take into account that emojis are double
    width

    
`rgbToHex(rgb)`
:   convert rgb tuple to hex