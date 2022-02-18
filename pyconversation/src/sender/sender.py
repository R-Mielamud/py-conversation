from typing import Callable, Dict, Union
from pyconversation.src.messages import BaseMessage, MessageTransfer
from pyconversation.src.loggers import BaseLogger
from pyconversation.src.types import MessageTransferGenerator

class MessageSender:
	logger: BaseLogger
	iterator: MessageTransferGenerator
	current_message: Union[MessageTransfer, None] = None
	resent_message: Union[MessageTransfer, None] = None
	send: Callable[[str], None]
	finished: bool = False

	def __init__(self, *, root: BaseMessage, logger: BaseLogger, send: Callable[[str], None]) -> None:
		self.logger = logger
		self.iterator = root.iterator(logger)
		self.send = send
		self._restore()

	def send_all_skippable(self, prev_answer: Union[str, None]) -> None:
		if self.resent_message is not None:
			self.send(self.resent_message.text)
			self.resent_message = None

			if not self.current_message.skip:
				return

		while True:
			try:
				self.current_message = self.iterator.send(prev_answer)
				self.send(self.current_message.text)
			except StopIteration:
				self.finished = True
				break

			if not self.current_message.skip:
				break

	def finalize(self) -> Dict[str, str]:
		self.iterator.close()

		result = self.logger.get_result_dict()
		self.logger.finalize()

		return result

	def _restore(self):
		last_id = self.logger.get_last_id()
		self.logger.reset_history()
		answer = None

		if last_id is not None:
			while True:
				try:
					self.current_message = self.iterator.send(answer)

					if self.current_message is None or self.current_message.id == last_id:
						break

					answer = self.logger.get(self.current_message.id)
				except StopIteration:
					self.finished = True
					break

		self.resent_message = self.current_message
