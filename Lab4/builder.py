from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class RobotBuilder(ABC):

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_body(self) -> None:
        pass

    @abstractmethod
    def produce_part_head(self) -> None:
        pass

    @abstractmethod
    def produce_part_libs1(self) -> None:
        pass

    @abstractmethod
    def produce_part_libs2(self) -> None:
        pass


class HumanoidRobot(RobotBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:

        product = self._product
        self.reset()
        return product

    def produce_part_body(self) -> None:
        self._product.add("Туловище")

    def produce_part_head(self) -> None:
        self._product.add("Голова")

    def produce_part_libs1(self) -> None:
        self._product.add("Руки")

    def produce_part_libs2(self) -> None:
        self._product.add("Ноги")

class AnimalRobot(RobotBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:

        product = self._product
        self.reset()
        return product

    def produce_part_body(self) -> None:
        self._product.add("Туловище")

    def produce_part_head(self) -> None:
        self._product.add("Голова")

    def produce_part_libs1(self) -> None:
        self._product.add("Передние лапы")

    def produce_part_libs2(self) -> None:
        self._product.add("Задние лапы")


class Product1():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        return f"Product parts: {', '.join(self.parts)}"


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> RobotBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: RobotBuilder) -> None:
        self._builder = builder

    def build_headless_robot(self) -> None:
        self.builder.produce_part_body()
        self.builder.produce_part_libs1()
        self.builder.produce_part_libs2()

    def build_full_robot(self) -> None:
        self.builder.produce_part_body()
        self.builder.produce_part_head()
        self.builder.produce_part_libs1()
        self.builder.produce_part_libs2()


if __name__ == "__main__":

    director = Director()
    HumanoidBuilder = HumanoidRobot()
    AnimalBuilder = AnimalRobot()
    director.builder = HumanoidBuilder

    print("Standart headless robot: ")
    director.build_headless_robot()
    print(HumanoidBuilder.product.list_parts())

    print("\n")

    print("Standard full robot: ")
    director.build_full_robot()
    print(HumanoidBuilder.product.list_parts())

    print("\n")

    print("Custom robot: ")
    HumanoidBuilder.produce_part_body()
    HumanoidBuilder.produce_part_libs2()
    print(HumanoidBuilder.product.list_parts())

    print("\n")

    director.builder = AnimalBuilder
    print("Standard full animal robot: ")
    director.build_full_robot()
    print(AnimalBuilder.product.list_parts())