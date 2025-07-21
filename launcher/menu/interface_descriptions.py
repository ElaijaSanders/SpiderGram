from re import compile

from Menu import MenuOption, Menu

# todo: hierarchy
mm_help = MenuOption(
    name="help",
    description="get help about launcher, concepts, interface, bots&userbots",
    pattern=compile(
        r"(h[ae]lp)|"
        r"(дов[іи]дка)|"
        r"(допомога)"
    ),
    
)
mm_launch = MenuOption(
    name="launch",
    description="launch SpiderGra for all connected accounts and bots along with their plugged additional modules",
    pattern=compile(
        r"(start)|(strat)|(lau?n((s?h?)|(c?h?)))|"
        r"(старт)|(ст?рат)|((за)?пуск)"
    )

)
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
mm_permissions = MenuOption(
    name="permissions",
    description="manage module permissions and access rights for specific accounts",
    pattern=compile(
        r"(permis?ions?)|"
        r"(дозв[іои]ли?)|"
        r"(права)|"
        r"(pm)|(mp)|([пд]м)"
    ),

)
mm_settings = MenuOption(
    name="settings",
    description="general launcher settings",
    pattern=compile(
        r"(gen[ae]ral{1,2}(.?set{1,2}ings?)?)|"
        r"((загальн[іи].?)?((параметри)|(опц[иі][иії])|(нала[шщ]туван{1,2}я)))"
    )

)
mm_about = MenuOption(
    name="about",
    description="authors, description, law info",
    pattern=compile(
        r"(about)|(info?)|(des[ck]r?(ipt(ion)?)?)|"
        r"((про.?)?автор([иі]|ство))"
    ),
)
mm_exit = MenuOption(
    name="exit",
    description="exit and stop the launcher",
    triggers=("exit", "quit", "stop"),
    pattern=compile(r":?[?!]?:?q!?"),

)
main_menu = Menu(
    (mm_launch, mm_help, mm_accounts, mm_account_options, mm_modules, mm_permissions, mm_settings, mm_about, mm_exit)
)

if __name__ == '__main__':
    print(
        '''testing, SPIDERGRAM bla-bla-bla
        bots&userbots
        *logo* or smth
        '''
    )
    main_menu.input_processor(break_after_valid=False)
