import json
import unittest
import mnist_sklearn_service

class ModelTest(unittest.TestCase):

    def test_mnist_predict(self):
        s = mnist_sklearn_service.MnistSklearnService("data/mnist/rf-93.pickle")
        with open("data/mnist/mnist_0.json") as f:
            matrix = json.load(f)
        res = s.predict(matrix)
        self.assertEqual(0, res)

    def test_mnist_predicts(self):
        s = mnist_sklearn_service.MnistSklearnService("data/mnist/rf-93.pickle")
        with open("data/mnist/mnist_0.json") as f:
            matrix0 = json.load(f)
        with open("data/mnist/mnist_1.json") as f:
            matrix1 = json.load(f)
        res = s.predicts([matrix0, matrix1])
        self.assertEqual([0, 1], res)
