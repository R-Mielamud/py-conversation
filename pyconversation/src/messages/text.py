from typing import Iterator
from pyconversation.src.enums import MessageType
from pyconversation.src.loggers import BaseLogger
from .base import BaseMessage
from .transfer import MessageTransfer


class Text(BaseMessage):
	text: str

	def __init__(self, *, id: str, text: str) -> None:
		super().__init__(id=id, type=MessageType.Text)
		self.text = text

	def iterator(self, logger: BaseLogger) -> Iterator[MessageTransfer]:
		yield MessageTransfer(text=self.text, skip=True)
