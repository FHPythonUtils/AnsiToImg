""" representation and processing of an ansi stream into an 'ast' of sorts
such that it can be rendered
"""
from ansitoimg.utils import ansiColourToRGB, findLen


class AnsiBlock():
	""" represent a block of ansi text. eg \033[31mhello!\033[0m

	ansi text can have the following attributes:
	- text
	- background colour
	- foreground colour
	- absolute char offset
	- bold
	- italic
	- underline
	- crossed out
	"""
	def __init__(self, text, position, bgColour=None, fgColour=None, bold=False,
	italic=False, underline=False, crossedOut=False):
		"""Constructor

		Args:
			text (string): text content to render
			position (int, int): x, y tuple to store the absolute offset in chars
			bgColour (string, optional): background colour. Defaults to None.
			fgColour (string, optional): foreground colour. Defaults to None.
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
	""" representation of ansi blocks

	ansi blocks has the following attributes:
	- ansi text
	- ansi blocks
	ansi blocks also holds a series of attributes that are used when processing
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
	def __init__(self, ansiText):
		"""Constructor

		Args:
			ansiText (string): ansi text stream to process
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
		""" process the ansi text into a series of ansi blocks """
		while self.pointer < len(self.ansiText):
			# process sgi codes
			if self.ansiText[self.pointer] == "\033":
				self.processSgi()
			# if not an sgi code then add to the text buffer
			else:
				self.textBuffer.append(self.ansiText[self.pointer])
				self.pointer += 1
			# if there is a 'closing' sgi code, create an ansi block
			if len(self.sgiBuffer) > 0 and self.sgiBuffer[-1] in ("\033[0m", "\033[21m",
			"\033[23m", "\033[24m", "\033[29m", "\033[39m", "\033[49m"):
				self.processCloseSgi()
		# create an ansi block out of anythin left over
		if len(self.textBuffer) > 0:
			self.setAnsiBlocks("".join(self.textBuffer))

	def setAnsiBlocks(self, text):
		"""create a series of ansi blocks from the text buffer and other attributes

		Args:
			text (string): text from the buffer
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
		# if text is before the sgi code. create an ansi block
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
		if sgiFlag == "\033[1m":
			self.bold = True
		elif sgiFlag in ("\033[2m", "\033[5m", "\033[6m", "\033[7m", "\033[8m", ):
			pass
		elif sgiFlag == "\033[3m":
			self.italic = True
		elif sgiFlag == "\033[4m":
			self.underline = True
		elif sgiFlag == "\033[9m":
			self.crossedOut = True
		elif sgiFlag != "\033[39m" and sgiFlag.startswith(
		"\033[3") or sgiFlag.startswith("\033[9"):
			self.fgColour = ansiColourToRGB(sgiFlag)
		elif sgiFlag != "\033[49m" and sgiFlag.startswith(
		"\033[4") or sgiFlag.startswith("\033[10"):
			self.bgColour = ansiColourToRGB(sgiFlag)
		self.sgiBuffer.append(sgiFlag)

	def processCloseSgi(self):
		""" process a closing sgi code and create ansi blocks accordingly
		reset any attributes that need setting """
		self.setAnsiBlocks("".join(self.textBuffer))
		# reset as per sgi code
		if self.sgiBuffer[-1] in ("\033[0m", "\033[49m"):
			self.bgColour = None
		if self.sgiBuffer[-1] in ("\033[0m", "\033[39m"):
			self.fgColour = None
		if self.sgiBuffer[-1] in ("\033[0m", "\033[21m"):
			self.bold = False
		if self.sgiBuffer[-1] in ("\033[0m", "\033[23m"):
			self.italic = False
		if self.sgiBuffer[-1] in ("\033[0m", "\033[24m"):
			self.underline = False
		if self.sgiBuffer[-1] in ("\033[0m", "\033[29m"):
			self.crossedOut = False
		self.textBuffer = []
		self.sgiBuffer = []
