"""
Handeler class.

Class for telegram bot register handlers
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Handler:
    callback: callable
    filters: List

    def check(self, message):
        state = True
        return state

    def notify(self, message):
        pass
