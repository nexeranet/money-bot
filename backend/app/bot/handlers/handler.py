"""
Handeler class.

Class for telegram bot register handlers
"""
from dataclasses import dataclass
from typing import List
from ..types.message import Message


@dataclass
class Handler:
    callback: callable
    filters: List

    def check(self, message: Message):
        if len(self.filters) == 0:
            return True
        state = False
        for i in range(len(self.filters)):
            if self.filters[i](message=message) is True:
                return True
        return state

    async def notify(self, message: Message):
        return await self.callback(message)
