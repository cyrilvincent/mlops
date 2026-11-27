import unittest
import config
import json
from sklearn_service import HouseSklearnService


class MyTestCase(unittest.TestCase):

    def test_first(self):
        i = 1
        i += 1
        self.assertEqual(2, i)

    def test_house_sklearn_service(self):
        service = HouseSklearnService(config.house_path)
        service.train()
        loyer = service.predict(100)
        self.assertEqual(3813, loyer)
        self.assertAlmostEqual(3800, loyer, delta=100)

    def test_house_sklearn_service_predicts(self):
        service = HouseSklearnService(config.house_path)
        service.train()
        loyers = service.predicts([10, 50, 100])
        self.assertAlmostEqual(126, loyers[0], delta=10)
        self.assertAlmostEqual(1765, loyers[1], delta=10)
        self.assertAlmostEqual(3813, loyers[2], delta=10)

    def test_cancer_sklearn(self):
        pass

    def test_mnist_sklearn(self):
        with open("data/mnist/mnist_0.json") as f:
            matrix0 = json.load(f)




