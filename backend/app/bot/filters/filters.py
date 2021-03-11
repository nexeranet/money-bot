from typing import List
from ..types.message import Message


def setCommands(commands: List = []):
    def check(message: Message):
        if message.is_bot_command() is False:
            return False
        text = message['text'][1:]
        print(text)
        for i in len(commands):
            print(i)
    return check


def setRegexp(regexp=None):
    pass
