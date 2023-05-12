from task_9_checks import Checks


class Input(Checks):
    def __init__(self, loc, text):
        self.text = text
        super().__init__(loc)



class Button(Checks):
    def __init__(self, loc, text):
        self.text = text
        super().__init__(loc)



class Link(Checks):
    def __init__(self, loc, text):
        self.text = text
        super().__init__(loc)



class Title(Checks):
    def __init__(self, loc, text):
        self.text = text
        super().__init__(loc)




my_obj_1 = Input('ksndkf8', 'hello')
my_obj_1.check_text()
my_obj_2 = Button('sandf8sd', 'next')
my_obj_2.check_text()
my_obj_3 = Link('fdsasd', 'fff')
my_obj_3.check_text()
my_obj_4 = Title('dsf', 'Go')
my_obj_4.check_text()
