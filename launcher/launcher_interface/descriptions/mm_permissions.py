from re import compile

from launcher.launcher_interface.Menu import MenuOption

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
