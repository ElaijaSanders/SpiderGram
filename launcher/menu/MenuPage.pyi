from typing import List, Tuple, Callable


class MenuPage:
    def __init__(
            self: MenuPage,
            text: str,
            process_user_input: Callable[[str], int | None] | Callable[[], int | None],
            father: MenuPage | None = None, children: List[MenuPage] | Tuple[MenuPage] | None = None
    ): ...