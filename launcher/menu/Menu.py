from collections.abc import Iterable, Callable, Sequence
from typing import List


class Formatter:
    __init__ = None

    @staticmethod
    def simple_left(text, size: int, filler: str = " "):
        text = str(text)
        if len(text) >= size:
            return text[:size]
        else:
            return f"{text}{filler*(size-len(text))}"

    @staticmethod
    def simple_right(text, size: int, filler: str = " "):
        text = str(text)
        if len(text) >= size:
            return text[:size]
        else:
            return f"{filler*(size-len(text))}{text}"


class MenuOption:
    __match_args__ = ("name", "triggers", "description", "body_func")

    def __init__(
            self,
            name: str,
            triggers: Sequence[str],  # todo: allow regex
            description: str = "",
            alt_func: Callable | None = None,
    ):
        self.description = description
        self.name = name
        self.triggers = list(triggers)
        if alt_func:
            self.body_func = alt_func

    def clone(self, mark_as_clone: bool = True):
        return MenuOption(
            name=f"{self.name}{' (Clone)' if mark_as_clone else ''}",
            triggers=self.triggers,
            description=f"{self.description}{' (Cloned)' if mark_as_clone else ''}",
            alt_func=self.body_func,
        )

    # region Alterable
    def body_func(self):
        print(f"hello from MenuOption {self.name}!\n{self.description}\n\n")
    # endregion


class Menu:
    __match_args__ = ("options", "input_processor", "get_input", "notification_invalid")

    def __init__(
            self,
            options: Iterable[MenuOption] = (),
            alt_processor: Callable | None = None,
            alt_input_getter: Callable | None = None,
            alt_notification: Callable | None = None,
    ):
        self.options: List[MenuOption] = []
        self.register_many(options)
        if alt_processor:
            self.input_processor = alt_processor
        if alt_input_getter:
            self.get_input = alt_input_getter
        if alt_notification:
            self.notification_invalid = alt_notification

    def register(self, option: MenuOption):
        o2 = option.clone(False)
        o2.triggers.append(str(len(self.options)))
        self.options.append(o2)

    def register_many(self, options: Iterable[MenuOption]):
        for o in options:
            self.register(o)

    # region Alterable
    def get_input(self, tab: int = 2):
        ll = len(str(len(self.options)))
        longest = max([len(o.name) for o in self.options])
        text = "Choose option from the list below:\n"
        for i, option in enumerate(self.options):
            text += (
                f"{tab * ' '}{Formatter.simple_right(i, ll)}. {Formatter.simple_left(option.name, longest)}"
                f"{f' | {option.description}' if option.description else ''}\n"
            )
        text += "Enter number or option's name: "
        return input(text)

    def notification_invalid(self, option: str):
        print(f"Invalid option: \"{option}\". Try again with valid option from the list\n")

    def input_processor(
            self,
            tab: int = 2,
            break_after_valid: bool = True,
            make_lower: bool = True,
            **option_parameters
    ):
        while True:
            choice = self.get_input(tab)
            print()
            if make_lower:
                choice = choice.lower()
            found = False
            for option in self.options:
                if choice in option.triggers:
                    option.body_func(**option_parameters)
                    found = True
            if found:
                if break_after_valid:
                    return
            else:
                self.notification_invalid(choice)
    # endregion


__all__ = ["MenuOption", "Menu"]
