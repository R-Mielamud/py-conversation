class MessageTransfer:
	text: str
	skip: bool

	def __init__(self, *, text: str, skip: bool) -> None:
		self.text = text
		self.skip = skip
