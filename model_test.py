import json
import unittest

import cancer_sklearn_service
import tensorflow_service
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

    def test_cancer_predict(self):
        s = cancer_sklearn_service.CancerSklearnService("data/cancer/rf-97.pickle")
        vector = [17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]
        res = s.predict(vector)
        self.assertEqual(1, res)

    def test_cancer_predicts(self):
        s = cancer_sklearn_service.CancerSklearnService("data/cancer/rf-97.pickle")
        matrix = [[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189],
                  [7.76,24.54,47.92,181,0.05263,0.04362,0,0,0.1587,0.05884,0.3857,1.428,2.548,19.15,0.007189,0.00466,0,0,0.02676,0.002783,9.456,30.37,59.16,268.6,0.08996,0.06444,0,0,0.2871,0.07039]]
        res = s.predicts(matrix)
        self.assertEqual([1,0], res)

    def test_imagenet_mobilenet(self):
        s = tensorflow_service.ImageNet()
        res, score = s.predict("data/img/mug.jpg")
        self.assertEqual("coffee_mug", res)
        self.assertAlmostEquals(0.7, score, delta=0.1)

    def test_dogsvscats_cnn(self):
        s = tensorflow_service.DogsVsCatsService("data/dogsvscats/cnn-77.h5")
        res, score = s.predict("data/dogsvscats/validation/cats/cat.1000.jpg")
        self.assertEqual("cat", res)

    def test_cancer_tf(self):
        s = tensorflow_service.CancerTFService("data/cancer/mlp.h5", "data/cancer/mlp_scaler.pickle")
        vector = [17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]
        res, score = s.predict(vector)
        self.assertEqual(1, res)