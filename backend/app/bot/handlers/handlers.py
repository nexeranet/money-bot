from typing import List
from .handler import Handler
from ..filters.filters import setCommands, setRegexp


class Handlers:
    """Base handlers class."""

    def __init__(self, api):
        self.api = api
        self.handlers: List = []

    def register(self, callback, commands=None, regexp=None):
        """register handler

        Args:
            callback: callback decorator
            commands: commands bot
            regexp: regexp message
            content_type: content type message
            state: state message
            run_task: run task bot
        """

        filters = []
        if(commands is not None):
            filters.append(setCommands(commands=commands))
        if(regexp is not None):
            filters.append(setRegexp(regexp=regexp))

        hander = Handler(callback=callback, filters=filters)
        self.handlers.append(hander)
        return ''

    async def notify(self, message):
        for handler in self.handlers:
            if(handler.check(message)):
                handler.notify(message)
                return True
        return False
