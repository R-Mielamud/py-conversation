from pyconversation.src.loggers import BaseLogger
from pyconversation.src.types import MessageTransferGenerator

class BaseMessage:
	id: str

	def __init__(self, *, id: str) -> None:
		self.id = id

	def iterator(self, logger: BaseLogger) -> MessageTransferGenerator:
		raise NotImplementedError()
