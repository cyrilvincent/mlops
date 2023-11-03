import tensorflow as tf
model = tf.keras.models.load_model("data/dogsvscats/cnn-77.h5")
model.summary()

batchSize = 16

trainset = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, validation_split=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

trainGenerator = trainset.flow_from_directory(
        'data/dogsvscats/large',
        target_size=(224, 224),
        subset = 'training',
        class_mode="binary",
        batch_size=batchSize)

validationGenerator = trainset.flow_from_directory(
        'data/dogsvscats/large',
        target_size=(224, 224),
        class_mode="binary",
        subset = 'validation',
        batch_size=batchSize)

model.fit(
        trainGenerator,
        epochs=200,
        validation_data=validationGenerator,
)

