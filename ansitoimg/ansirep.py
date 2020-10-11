""" representation and processing of an ANSI stream into an 'ast' of sorts
such that it can be rendered
"""
from __future__ import annotations
from typing import Optional

from ansitoimg.utils import ansiColourToRGB, findLen


class AnsiBlock():
	""" represent a block of ANSI text. eg \033[31mhello!\033[0m

	ANSI text can have the following attributes:
	- text
	- background colour
	- foreground colour
	- absolute char offset
	- bold
	- italic
	- underline
	- crossed out
	"""
	def __init__(self, text: str, position: tuple[int, int],
	bgColour: Optional[str]=None, fgColour: Optional[str]=None, bold: bool=False,
	italic: bool=False, underline: bool=False, crossedOut: bool=False):
		"""Constructor

		Args:
			text (str): text content to render
			position (int, int): x, y tuple to store the absolute offset in chars
			bgColour (str, optional): background colour. Defaults to None.
			fgColour (str, optional): foreground colour. Defaults to None.
			bold (bool, optional): is text bold?. Defaults to False.
			italic (bool, optional): is text italic?. Defaults to False.
			underline (bool, optional): is text underlined?. Defaults to False.
			crossedOut (bool, optional): is text crossed out?. Defaults to False.
		"""
		self.text = text
		self.bgColour = bgColour
		self.fgColour = fgColour
		self.bold = bold
		self.italic = italic
		self.underline = underline
		self.crossedOut = crossedOut
		self.position = position


class AnsiBlocks():
	""" representation of ANSI blocks

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
	"""
	def __init__(self, ansiText: str):
		"""Constructor

		Args:
			ansiText (str): ANSI text stream to process
		"""
		# text to parse
		self.ansiText = ansiText
		# list of blocks
		self.ansiBlocks = []
		# track various attributes
		self.sgiBuffer = []
		self.textBuffer = []
		self.bold = False
		self.italic = False
		self.underline = False
		self.crossedOut = False
		self.bgColour = None
		self.fgColour = None
		self.absX = 0
		self.absY = 0

		self.height = 1
		self.pointer = 0

	def process(self):
		""" process the ANSI text into a series of ANSI blocks """
		while self.pointer < len(self.ansiText):
			# process sgi codes
			if self.ansiText[self.pointer] == "\033":
				self.processSgi()

			# if not an sgi code then add to the text buffer
			else:
				self.textBuffer.append(self.ansiText[self.pointer])
				self.pointer += 1
			# if there is a 'closing' sgi code, create an ANSI block
			if len(self.sgiBuffer) > 0 and self.sgiBuffer[-1] in ("\033[0m", "\033[00m", "\033[21m",
			"\033[23m", "\033[24m", "\033[29m", "\033[39m", "\033[49m"):
				self.processCloseSgi()
		# create an ANSI block out of anythin left over
		if len(self.textBuffer) > 0:
			self.setAnsiBlocks("".join(self.textBuffer))

	def setAnsiBlocks(self, text: str):
		"""create a series of ANSI blocks from the text buffer and other attributes

		Args:
			text (str): text from the buffer
		"""
		writeTxt = []
		for char in text:
			if char == "\n" or self.absX + findLen(writeTxt) > 59: # triggers a newline
				self.ansiBlocks.append(
				AnsiBlock("".join(writeTxt), (self.absX, self.absY), self.bgColour,
				self.fgColour, self.bold, self.italic))
				self.absX = 0
				self.absY += 1
				self.height += 1
				writeTxt = []
			if char != "\n":
				writeTxt.append(char)
		if findLen(writeTxt) > 0:
			self.ansiBlocks.append(
			AnsiBlock("".join(writeTxt), (self.absX, self.absY), self.bgColour,
			self.fgColour, self.bold, self.italic, self.underline, self.crossedOut))
			self.absX += findLen(writeTxt)
		self.textBuffer = []

	def processSgi(self):
		""" process an sgi code and set attributes accordingly """
		# if text is before the sgi code. create an ANSI block
		if len(self.textBuffer) > 0:
			self.setAnsiBlocks("".join(self.textBuffer))
		sgiChar = []
		# 'm' is used to mark the end of an sgi code. read to the end
		while self.ansiText[self.pointer] != "m":
			sgiChar.append(self.ansiText[self.pointer])
			self.pointer += 1
		sgiChar.append(self.ansiText[self.pointer])
		self.pointer += 1
		# set attributes based on the sgi flag
		sgiFlag = "".join(sgiChar)
		if sgiFlag in ("\033[1m", "\033[01m"):
			self.bold = True
		elif sgiFlag in ("\033[2m", "\033[5m", "\033[6m", "\033[7m", "\033[8m",
		"\033[02m", "\033[05m", "\033[06m", "\033[07m", "\033[08m", ):
			pass
		elif sgiFlag in ("\033[3m", "\033[03m"):
			self.italic = True
		elif sgiFlag in ("\033[4m", "\033[04m"):
			self.underline = True
		elif sgiFlag in ("\033[9m", "\033[09m"):
			self.crossedOut = True
		elif sgiFlag != "\033[39m" and sgiFlag.startswith(
		"\033[3") or sgiFlag.startswith("\033[9"):
			self.fgColour = ansiColourToRGB(sgiFlag)
		elif sgiFlag != "\033[49m" and sgiFlag.startswith(
		"\033[4") or sgiFlag.startswith("\033[10"):
			self.bgColour = ansiColourToRGB(sgiFlag)
		self.sgiBuffer.append(sgiFlag)

	def processCloseSgi(self):
		""" process a closing sgi code and create ANSI blocks accordingly
		reset any attributes that need setting """
		self.setAnsiBlocks("".join(self.textBuffer))
		# reset as per sgi code
		if self.sgiBuffer[-1] in ("\033[0m", "\033[00m", "\033[49m"):
			self.bgColour = None
		if self.sgiBuffer[-1] in ("\033[0m", "\033[00m", "\033[39m"):
			self.fgColour = None
		if self.sgiBuffer[-1] in ("\033[0m", "\033[00m", "\033[21m"):
			self.bold = False
		if self.sgiBuffer[-1] in ("\033[0m", "\033[00m", "\033[23m"):
			self.italic = False
		if self.sgiBuffer[-1] in ("\033[0m", "\033[00m", "\033[24m"):
			self.underline = False
		if self.sgiBuffer[-1] in ("\033[0m", "\033[00m", "\033[29m"):
			self.crossedOut = False
		self.textBuffer = []
		self.sgiBuffer = []
