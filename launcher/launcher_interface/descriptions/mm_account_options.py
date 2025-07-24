from re import compile

from launcher.launcher_interface.Menu import MenuOption

mm_account_options = MenuOption(
    name="account options",
    description="account-specific settings and userbot permissions",
    pattern=compile(
        r"(ac{0,2}[ao]unt.?((options?)|(set{1,2}ings?)))|"
        r"(ao)|(as)|"
        r"(((параметри)|(опц[иі][иії])|(нала[шщ]туван{1,2}я)).?ак{1,2}аунт[иі]в)|"
        r"(па)|(оа)|(на)"
    ),

)
