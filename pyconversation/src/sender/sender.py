from typing import Callable, Dict, Union
from pyconversation.src.messages import BaseMessage, MessageTransfer
from pyconversation.src.loggers import BaseLogger
from pyconversation.src.types import MessageTransferGenerator

class MessageSender:
	logger: BaseLogger
	iterator: MessageTransferGenerator
	current_message: MessageTransfer
	send: Callable[[str], None]
	finished: bool = False

	def __init__(self, *, root: BaseMessage, logger: BaseLogger, send: Callable[[str], None]) -> None:
		self.logger = logger
		self.iterator = root.iterator(logger)
		self.send = send
		self._restore()

	def send_all_skippable(self, prev_answer: Union[str, None]) -> None:
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
		return self.logger.get_result_dict()

	def _restore(self):
		last_id = self.logger.get_last_id()
		self.logger.reset_history()

		if last_id is not None:
			while self.current_message is not None and self.current_message.id != last_id:
				answer = self.logger.get(self.current_message.id)

				try:
					self.current_message = self.iterator.send(answer)
				except StopIteration:
					self.finished = True
					break
