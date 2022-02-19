from typing import Generator, Union
from messages.transfer import MessageTransfer


MessageTransferGenerator = Generator[MessageTransfer, Union[str, None], None]
