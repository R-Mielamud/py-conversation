from typing import Dict
from .base import BaseLogger


class DictLogger(BaseLogger):
	result: Dict[str, str] = dict()

	def log(self, key: str, value: str) -> None:
		self.result[key] = value
