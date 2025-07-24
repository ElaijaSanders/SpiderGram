from re import compile

from launcher.launcher_interface.Menu import MenuOption

mm_settings = MenuOption(
    name="settings",
    description="general launcher settings",
    pattern=compile(
        r"(gen[ae]ral{1,2}(.?set{1,2}ings?)?)|"
        r"((загальн[іи].?)?((параметри)|(опц[иі][иії])|(нала[шщ]туван{1,2}я)))"
    )

)
