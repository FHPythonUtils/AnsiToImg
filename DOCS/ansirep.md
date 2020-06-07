Module ansitoimg.ansirep
========================
representation and processing of an ANSI stream into an 'ast' of sorts
such that it can be rendered

Classes
-------

`AnsiBlock(text, position, bgColour=None, fgColour=None, bold=False, italic=False, underline=False, crossedOut=False)`
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
            text (string): text content to render
            position (int, int): x, y tuple to store the absolute offset in chars
            bgColour (string, optional): background colour. Defaults to None.
            fgColour (string, optional): foreground colour. Defaults to None.
            bold (bool, optional): is text bold?. Defaults to False.
            italic (bool, optional): is text italic?. Defaults to False.
            underline (bool, optional): is text underlined?. Defaults to False.
            crossedOut (bool, optional): is text crossed out?. Defaults to False.

`AnsiBlocks(ansiText)`
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
            ansiText (string): ANSI text stream to process

    ### Methods

    `process(self)`
    :   process the ANSI text into a series of ANSI blocks

    `processCloseSgi(self)`
    :   process a closing sgi code and create ANSI blocks accordingly
        reset any attributes that need setting

    `processSgi(self)`
    :   process an sgi code and set attributes accordingly

    `setAnsiBlocks(self, text)`
    :   create a series of ANSI blocks from the text buffer and other attributes
        
        Args:
                text (string): text from the buffer