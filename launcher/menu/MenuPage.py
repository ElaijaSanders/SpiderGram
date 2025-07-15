class MenuPage:
    class MenuException(Exception):
        def __init__(self, *args):
            super().__init__(*args)

    ready_pages = []
    active_page = None

    @staticmethod
    def __getitem__(item):
        return MenuPage.ready_pages[item]

    def __init__(
            self,
            text,
            input_processor=None,
            transitions_map=None
    ):
        self.input_processor = input_processor
        self.transitions_map = transitions_map
        self.text = text
        self.id = len(self.ready_pages)
        MenuPage.ready_pages.append(self)

    def activate(self):
        if MenuPage.active_page is not None:
            raise self.MenuException(
                f"I/O is already occupied by another page with ID={MenuPage.active_page.id}. Deactivate it first"
            )
        MenuPage.active_page = self
        print(self.text)

    @staticmethod
    def deactivate():
        MenuPage.active_page = None

    # TODO: ???
    '''def do_smth_with_input(self):
        if not (bool(self.transitions_map) or bool(self.input_processor)):
            self.deactivate()
            return
            # todo possible deadlock?
        answer = input()
        result = None
        if bool(self.input_processor):
            result = self.input_processor(answer, self)
        if bool(self.transitions_map):
            query = result or answer 
    '''
