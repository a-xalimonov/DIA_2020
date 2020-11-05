from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    figure1 = Rectangle("чёрный", 3, 2)
    figure3 = Square("серый", 5)
    figure2 = Circle("белый", 5)

    print()
    print(figure1,'\n')
    print(figure2,'\n')
    print(figure3)

if __name__ == "__main__":
    main()