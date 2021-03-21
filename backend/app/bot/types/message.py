from dataclasses import dataclass
from typing import Dict


@dataclass
class Message:
    send_function: callable
    content: Dict

    def get_text(self):
        return self.content['text']

    def get_bot_command(self):
        return self.get_text()[1:]

    def is_bot_command(self):
        if self.content.get('entities') is None:
            return False
        if self.content['entities'][0]['type'] != 'bot_command':
            return False
        return True

    async def send(self, content):
        id = self.content['chat']['id']
        await self.send_function(id, content)
        pass
