from launcher.launcher_interface.Menu import Menu
from launcher.launcher_interface.descriptions.mm_about import mm_about
from launcher.launcher_interface.descriptions.mm_account_options import mm_account_options
from launcher.launcher_interface.descriptions.mm_accounts import mm_accounts
from launcher.launcher_interface.descriptions.mm_exit import mm_exit
from launcher.launcher_interface.descriptions.mm_help import mm_help
from launcher.launcher_interface.descriptions.mm_launch import mm_launch
from launcher.launcher_interface.descriptions.mm_modules import mm_modules
from launcher.launcher_interface.descriptions.mm_permissions import mm_permissions
from launcher.launcher_interface.descriptions.mm_settings import mm_settings

main_menu = Menu(
    (mm_launch, mm_help, mm_accounts, mm_account_options, mm_modules, mm_permissions, mm_settings, mm_about, mm_exit)
)


def main_page():
    print(
        '''testing, SPIDERGRAM bla-bla-bla
        bots&userbots
        *logo* or smth
        '''
    )
    main_menu.input_processor(break_after_valid=False)


if __name__ == '__main__':
    main_page()
