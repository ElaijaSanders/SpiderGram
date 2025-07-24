from re import compile

from launcher.launcher_interface.Menu import MenuOption

mm_exit = MenuOption(
    name="exit",
    description="exit and stop the launcher",
    triggers=("exit", "quit", "stop"),
    pattern=compile(r":?[?!]?:?q!?"),

)
