from dataclasses import dataclass
from typing import Dict
from ..bot import Bot


@dataclass
class Message:
    bot: Bot
    content: Dict

    def get_bot_command(self):
        return self.content['text'][1:]

    def is_bot_command(self):
        if self.content.get('entities') is None:
            return False
        if self.content['entities']['type'] != 'bot_command':
            return False
        return True

    async def send(self, content):
        id = self.content['chat']['id']
        await self.bot.sendMessage(id, content)
        pass
