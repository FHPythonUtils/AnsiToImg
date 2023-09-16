# monospaced chars have a constant height and width
TEXT_HEIGHT = 21
TEXT_WIDTH = 12

WIDTH_DEFAULT = 49
WIDTH_WIDE = 89

TITLE = "AnsiToImg (courtesy of Rich)"


def _resolveWidth(wide: bool, width: int = 49):
	width = int(width)
	if width == 49 and wide:
		return 89
	return width
