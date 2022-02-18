class MessageTransfer:
	text: str
	skip: bool
	terminate_group: bool

	def __init__(self, *, text: str, skip: bool = False, terminate_group: bool = False) -> None:
		self.text = text
		self.skip = skip
		self.terminate_group = terminate_group
