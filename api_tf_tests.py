import unittest
from fastapi.testclient import TestClient
import api_tf
import json


class ApiTFTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(api_tf.app)

    def test_root(self):
        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)

    def test_cancer(self):
        x = [17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]
        r = self.client.post("/cancer", json=x)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()[0], 1)

    def test_mnist(self):
        with open("data/mnist/mnist_0.json") as f:
            x = json.load(f)
        r = self.client.post("/mnist", json=x)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()[0], 0)

