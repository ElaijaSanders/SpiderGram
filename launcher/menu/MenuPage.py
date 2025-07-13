class MenuPage:
    def __init__(
            self,
            text,
            process_user_input,
            father=None, children=None
    ):
        self.processUserInput = process_user_input
        self.text = text
        self.father = father
        self.children = list(children)

