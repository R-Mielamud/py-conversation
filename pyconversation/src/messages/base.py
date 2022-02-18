from typing import Iterator
from pyconversation.src.enums import MessageType
from pyconversation.src.loggers import BaseLogger
from .transfer import MessageTransfer

class BaseMessage:
	id: str
	type: MessageType

	def __init__(self, *, id: str, type: MessageType) -> None:
		self.id = id
		self.type = type

	def iterator(self, logger: BaseLogger) -> Iterator[MessageTransfer]:
		raise NotImplementedError()
