import re


def input_until_valid(
        pattern: str = "",
        initial_prompt: str = "",
        prompt_on_invalid: str = "",
        *,
        make_lower: bool = True,
) -> str:
    print(initial_prompt, end="")
    while True:
        result = input("> ")
        if make_lower:
            result = result.lower()
        if re.fullmatch(pattern, result):
            return result
        print(prompt_on_invalid)


def help_me():
    print("Hello from help")


def modules():
    print("Hello from modules")


def module_permissions():
    print("Hello from permissions")


def accounts():
    print("Hello from accounts")


def general_settings():
    print("hello from general settings")


def finish():
    print("hello from quit")
    exit(0)


def mainloop():
    print(
        '''testing, SPIDERGRAM bla-bla-bla
        bots&userbots
        *logo* or smth
        '''
    )
    while True:
        match option := input(
            "\nChoose option (enter number or option name):\n"
            "  1. help\n"
            "  2. modules\n"
            "  3. permissions\n"
            "  4. accounts\n"
            "  5. settings\n"
            "  6. exit\n"
            ": >"
        ):
            case x if x in (1, "help"):
                help_me()
            case x if x in (2, "modules"):
                modules()
            case x if x in (3, "permissions"):
                module_permissions()
            case x if x in (4, "accounts"):
                accounts()
            case x if x in (5, "settings"):
                general_settings()
            case x if x in (6, "exit"):
                finish()
            case _:
                print(f"Unknown option: \"{option}\". Try again with valid option from below")


mainloop()
