from keras.applications import ResNet152V2
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2


class ImageNet:

    def __init__(self):
        self.model = MobileNetV2()

    def predict(self, path):
        image = load_img(path, target_size=(224, 224))
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)
        yhat = self.model.predict(image)
        label = decode_predictions(yhat)
        label = label[0][0]
        return label[1], float(label[2])

