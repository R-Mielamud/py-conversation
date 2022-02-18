from typing import Generator, Union
from pyconversation.src.messages.transfer import MessageTransfer


MessageTransferGenerator = Generator[MessageTransfer, Union[str, None], None]
