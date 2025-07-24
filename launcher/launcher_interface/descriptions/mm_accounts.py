from re import compile

from launcher.launcher_interface.Menu import MenuOption

mm_accounts = MenuOption(
    name="accounts",
    description="manage accounts and bots that are operated by this launcher: login, logout",
    pattern=compile(
        r"(ac{0,2}[ao]unts?)|"
        r"((user)?bots?)|"
        r"(ак{1,2}(аунт)?и?)|"
        r"(юзер)?боти?"
    ),

)
