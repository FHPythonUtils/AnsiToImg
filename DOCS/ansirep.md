Module ansitoimg.ansirep
========================
representation and processing of an ANSI stream into an 'ast' of sorts
such that it can be rendered

Classes
-------

`AnsiBlock(text: str, position: tuple[int, int], bgColour: Optional[str] = None, fgColour: Optional[str] = None, bold: bool = False, italic: bool = False, underline: bool = False, crossedOut: bool = False)`
:   represent a block of ANSI text. eg [31mhello![0m
    
    ANSI text can have the following attributes:
    - text
    - background colour
    - foreground colour
    - absolute char offset
    - bold
    - italic
    - underline
    - crossed out
    
    Constructor
    
    Args:
            text (str): text content to render
            position (int, int): x, y tuple to store the absolute offset in chars
            bgColour (str, optional): background colour. Defaults to None.
            fgColour (str, optional): foreground colour. Defaults to None.
            bold (bool, optional): is text bold?. Defaults to False.
            italic (bool, optional): is text italic?. Defaults to False.
            underline (bool, optional): is text underlined?. Defaults to False.
            crossedOut (bool, optional): is text crossed out?. Defaults to False.

`AnsiBlocks(ansiText: str, wide: bool = True)`
:   representation of ANSI blocks
    
    ANSI blocks has the following attributes:
    - ANSI text
    - ANSI blocks
    ANSI blocks also holds a series of attributes that are used when processing
    - sgi buffer
    - text buffer
    - background colour
    - foreground colour
    - absolute char offset
    - bold
    - italic
    - underline
    - crossed out
    - height
    - char pointer
    
    Constructor
    
    Args:
            ansiText (str): ANSI text stream to process
            wide (bool, optional): use a 'wide' terminal 89 vs 49 chars

    ### Methods

    `process(self)`
    :   process the ANSI text into a series of ANSI blocks

    `processCloseSgi(self)`
    :   process a closing sgi code and create ANSI blocks accordingly
        reset any attributes that need setting

    `processSgi(self)`
    :   process an sgi code and set attributes accordingly

    `setAnsiBlocks(self, text: str)`
    :   create a series of ANSI blocks from the text buffer and other attributes
        
        Args:
                text (str): text from the buffer