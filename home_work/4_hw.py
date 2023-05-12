
'''
class Rectangle:
    def __init__(self, width, height):
        self.weidth = width
        self.height =height

    def square(self):
        print(f'Площадь равна {self.weidth * self.height}')

    def perimeter(self):
        print(f'Периметр равен {(self.weidth + self.height)*2}')



rectangle_1 = Rectangle(3, 4)
rectangle_1.square()
rectangle_1.perimeter()
rectangle_2 = Rectangle(5, 6)
rectangle_2.square()
rectangle_2.perimeter()
rectangle_3 = Rectangle(34, 22)
rectangle_3.square()
rectangle_3.perimeter()




class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    @staticmethod
    def addition(a, b):
        print(a + b)

    @staticmethod
    def multiplication(a, b):
        print(a * b)

    @staticmethod
    def division(a, b):
        print(a / b)

    @staticmethod
    def subtraction(a, b):
        print(a - b)


Math.addition(1, 4)
Math.multiplication(1, 4)
Math.division(1, 4)
Math.subtraction(1, 4)

'''


class Demoqa_elements:

    def __init__(self, text, type_, locator = '' ):
        self.text = text
        self.type_ = type_
        self.locator = locator


    def __str__(self):
        return f"Text: {self.text}"


    def push_button(self):
        print(f'Клик по кнопке {self.text}')


elemants_buttons_text = ['Text Box', 'Check Box', 'Radoi Button', 'Web Tables', 'Buttons', 'Links', 'Broken Links Images', 'Upload and Download', 'Dynamic Properties']

for i in elemants_buttons_text:
    a = Demoqa_elements(i, 'button')
    print(a)
    a.push_button()
