from re import compile

from launcher.launcher_interface.Menu import MenuOption

mm_about = MenuOption(
    name="about",
    description="authors, description, law info",
    pattern=compile(
        r"(about)|(info?)|(des[ck]r?(ipt(ion)?)?)|"
        r"((про.?)?автор(([иі]в?)|(ство)))"
    ),
)
