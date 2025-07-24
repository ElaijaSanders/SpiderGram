from re import compile

from launcher.launcher_interface.Menu import MenuOption

mm_help = MenuOption(
    name="help",
    description="get help about launcher, concepts, interface, bots&userbots",
    pattern=compile(
        r"(h[ae]lp)|"
        r"(дов[іи]дка)|"
        r"(допомога)"
    ),

)
