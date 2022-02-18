from typing import List
from pyconversation.src.loggers import BaseLogger
from pyconversation.src.types import MessageTransferGenerator
from .base import BaseMessage
from .transfer import MessageTransfer

class Group(BaseMessage):
	children: List[BaseMessage]

	def __init__(self, *, id: str, children: List[BaseMessage]) -> None:
		super().__init__(id=id)
		self.children = children
	
	def iterator(self, logger: BaseLogger) -> MessageTransferGenerator:
		for child in self.children:
			iterator = child.iterator(logger)
			prev_answer = None

			try:
				while True:
					message = iterator.send(prev_answer)

					if message.terminate_group:
						yield MessageTransfer(text=message.text, skip=True)
						break

					prev_answer = yield message
				else:
					continue

				break
			except StopIteration:
				pass
