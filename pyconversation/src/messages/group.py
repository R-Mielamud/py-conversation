from typing import Iterator, List
from pyconversation.src.enums import MessageType
from pyconversation.src.loggers import BaseLogger
from .base import BaseMessage
from .transfer import MessageTransfer

class Group(BaseMessage):
	children: List[BaseMessage]

	def __init__(self, *, id: str, children: List[BaseMessage]) -> None:
		super().__init__(id=id, type=MessageType.Group)
		self.children = children
	
	def iterator(self, logger: BaseLogger) -> Iterator[MessageTransfer]:
		for child in self.children:
			yield from child.iterator(logger)
