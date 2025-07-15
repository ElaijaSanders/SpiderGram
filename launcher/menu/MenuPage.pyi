from collections.abc import Mapping, Callable
from typing import List, SupportsIndex, Any


class MenuPage:
    ready_pages: List[MenuPage]
    active_page: MenuPage|None

    @staticmethod
    def __getitem__(self, item: SupportsIndex) -> MenuPage: ...

    def __init__(
            self,
            text: str,
            input_processor: Callable[[str, MenuPage], Any] = None,
            transitions_map: Mapping[str, int] = None
    ):
        self.input_processor = input_processor
        self.transitions_map = transitions_map
        self.text = text
        self.id = len(self.ready_pages)
        MenuPage.ready_pages.append(self)