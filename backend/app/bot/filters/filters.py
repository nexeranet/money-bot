from typing import List
from ..types.message import Message


def setCommands(commands: List = []):
    def check(message: Message):
        if message.is_bot_command() is False:
            return False
        text = message.get_bot_command()
        for i in range(len(commands)):
            if(commands[i] == text):
                return True
        return False
    return check


def setRegexp(regexp=None):
    def check(message: Message):
        return False
    return check
