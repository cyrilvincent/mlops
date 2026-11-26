import keras

model = keras.applications.MobileNetV2()

image = keras.utils.load_img("data/img/ski.jpg", target_size=(224, 224))
image = keras.utils.img_to_array(image)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
image = keras.applications.resnet_v2.preprocess_input(image)
yhat = model.predict(image)
label = keras.applications.resnet_v2.decode_predictions(yhat)
label = label[0][0]
print(label[1], float(label[2]))