from re import compile

from launcher.launcher_interface.Menu import MenuOption

mm_modules = MenuOption(
    name="modules",
    description="manage modules: download, update, delete",
    pattern=compile(
        r"(modules?.?(manager)?)|"
        r"(модул[ьіяи]в?.?(менед?жер)?)|"
        r"((менед?жер)?.?(модул[ьіяи]в?))|"
        r"(mm)|(мм)"
    ),

)
