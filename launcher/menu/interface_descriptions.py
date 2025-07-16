from Menu import MenuOption, Menu

# todo: hierarchy
mm_help = MenuOption(
    name="help",
    description="get help about launcher, concepts, interface, bots&userbots",
    triggers=("help", "halp", "hlep", "довідка", "довидка", "допомога"),
    
)
# todo: launch
mm_accounts = MenuOption(
    name="accounts",
    description="manage accounts and bots that are operated by this launcher: login, logout",
    triggers=(
        "accounts", "accounts", "account", "acount", "acc", "ac", "bots", "bot"
        "акаунти", "аккаунти", "акаунт", "аккаунт", "ак", "акк", "аки", "акки", "бот", "боти"
    ),

)
mm_account_options = MenuOption(
    name="account options",
    description="account-specific settings and userbot permissions",
    triggers=(
        "account options", "accountoptions", "account_options", "account-options",
        "acount options", "acountoptions", "acount_options", "acount-options",
        "account setings", "accountsetings", "account_setings", "account-setings",
        "acount setings", "acountsetings", "acount_setings", "acount-setings",
        "account settings", "accountsettings", "account_settings", "account-settings",
        "acount settings", "acountsettings", "acount_settings", "acount-settings",
        "ao", "as",
    ),

)
mm_modules = MenuOption(
    name="modules",
    description="manage modules: download, update, delete",
    triggers=(
        "module", "modules", "модуль", "модулі",
        "module manager", "modules manager", "module_manager", "modules_manager", "mm",
        "модуль менеджер", "модуль_менеджер", "модуль-менеджер", "менеджер модулів", "мм"
    ),

)
mm_permissions = MenuOption(
    name="permissions",
    description="manage module permissions and access rights for specific accounts",
    triggers=("permissions", "permisions", "mp", "дозволи", "дозвіл", "права", "пм", "дм"),

)
mm_settings = MenuOption(
    name="settings",
    description="general launcher settings",
    triggers=("settings", "sets", "st"),

)
# todo: about
mm_exit = MenuOption(
    name="exit",
    description="exit and stop the launcher",
    triggers=("exit", "quit", "stop")
)
main_menu = Menu(
    (mm_help, mm_accounts, mm_account_options, mm_modules, mm_permissions, mm_settings, mm_exit)
)

if __name__ == '__main__':
    print(
        '''testing, SPIDERGRAM bla-bla-bla
        bots&userbots
        *logo* or smth
        '''
    )
    main_menu.input_processor(break_after_valid=False)
