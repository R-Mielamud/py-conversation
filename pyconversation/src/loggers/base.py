from typing import Dict, Union


class BaseLogger:
	def log(self, id: str, value: str) -> None:
		raise NotImplementedError()

	def get(self, id: str) -> None:
		raise NotImplementedError()

	def get_result_dict(self) -> Dict[str, str]:
		raise NotImplementedError()

	def reset_history(self, id: str) -> None:
		pass

	def log_last_id(self, id: str) -> None:
		pass

	def get_last_id(self) -> Union[str, None]:
		pass
