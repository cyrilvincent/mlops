import unittest
from sklearn_service import HouseSklearnService

class ServiceTest(unittest.TestCase):

    def test_bidon(self):
        # Initialiser une variable
        i = 1
        # Faire une action
        i += 1
        # Faire un assert
        self.assertEqual(2, i)

    def test_house_sklearn_service(self):
        house_service = HouseSklearnService("data/house/house.csv")
        house_service.train()
        loyer = house_service.predict(100)
        self.assertEqual(3813, loyer)
