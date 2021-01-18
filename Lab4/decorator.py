class Component():

    def operation(self) -> str:
        pass

    def __init__(self):
        pass


class Student(Component):

    def operation(self) -> str:
        return f"Студент: {self._lastname} {self._firstname}"

    def __init__(self, lastname, firstname):
        self._lastname = lastname
        self._firstname = firstname


class Decorator(Component):

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:

        return self._component

    def operation(self) -> str:

        return self._component.operation()


class IU_department(Decorator):

    def operation(self) -> str:
        
        return f"{self.component.operation()}, факультет ИУ"

class SM_department(Decorator):

    def operation(self) -> str:
        
        return f"{self.component.operation()}, факультет СМ"


class IU5(Decorator):

    def operation(self) -> str:
        return f"{self.component.operation()}, кафедра ИУ5"

class IU10(Decorator):

    def operation(self) -> str:
        return f"{self.component.operation()}, кафедра ИУ10"
        
class SM1(Decorator):

    def operation(self) -> str:
        return f"{self.component.operation()}, кафедра СМ1"


if __name__ == "__main__":
    
    print('\n')
    Student1 = Student("Халимонов", "Антон")
    Student2 = Student("Терентьев", "Максим")
    Student3 = Student("Перлин", "Алексей")
    print("До добавления декоратора:")
    print(Student1.operation())
    print(Student2.operation())
    print(Student3.operation())
    print('\n')

    Student1_d = IU_department(Student1)
    Student1_dc = IU5(Student1_d)

    Student2_d = IU_department(Student1)
    Student2_dc = IU10(Student1_d)

    Student3_d = SM_department(Student1)
    Student3_dc = SM1(Student1_d)
    
    print("После добавления декотратора:")
    print(Student1_dc.operation())
    print(Student2_dc.operation())
    print(Student3_dc.operation())