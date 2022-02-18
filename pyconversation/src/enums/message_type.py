from enum import Enum


class MessageType(Enum):
	Text = "text"
	Group = "group"
	Ask = "ask"
	Switch = "switch"
	List = "list"
