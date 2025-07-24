from re import compile

from launcher.launcher_interface.Menu import MenuOption

mm_launch = MenuOption(
    name="launch",
    description="launch SpiderGram for all connected accounts and bots along with their plugged additional modules",
    pattern=compile(
        r"(start)|(strat)|(lau?n((s?h?)|(c?h?)))|"
        r"(старт)|(ст?рат)|((за)?пуск)"
    )

)
