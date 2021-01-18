from builder import HumanoidRobot, AnimalRobot
import unittest


class SetTest(unittest.TestCase):
    def setUp(self):
        self.humanoid_robot = HumanoidRobot()
        self.animal_robot = AnimalRobot()

    def test_humanoid_body(self):
        self.humanoid_robot.produce_part_body()
        self.assertEqual(self.humanoid_robot.product.list_parts(), "Product parts: Туловище")

    def test_animal_body_and_libs(self):
        self.animal_robot.produce_part_body()
        self.animal_robot.produce_part_libs1()
        self.animal_robot.produce_part_libs2()
        self.assertEqual(self.animal_robot.product.list_parts(), "Product parts: Туловище, Передние лапы, Задние лапы")


if __name__ == "__main__":
    unittest.main()