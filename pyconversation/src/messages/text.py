from pyconversation.src.loggers import BaseLogger
from pyconversation.src.types import MessageTransferGenerator
from .base import BaseMessage
from .transfer import MessageTransfer


class Text(BaseMessage):
	text: str

	def __init__(self, *, id: str, text: str) -> None:
		super().__init__(id=id)
		self.text = text

	def iterator(self, logger: BaseLogger) -> MessageTransferGenerator:
		yield MessageTransfer(text=self.text, skip=True)
