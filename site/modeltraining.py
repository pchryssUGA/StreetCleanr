import tensorflow as tf
import os
import cv2
import imghdr
from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
from tensorflow.keras.models import load_model

# Limit GPU memory usage
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


# Load the model
data_dir = os.path.join('site','static', 'testing', 'data')
image_exts = ['jpeg', 'jpg', 'png', 'bmp']

for image_class in os.listdir(data_dir):
    if image_class == '.DS_Store':
        os.remove(os.path.join(data_dir, image_class))
        continue
    if image_class == 'trash' or image_class == 'new':
        continue
    for image in os.listdir(os.path.join(data_dir, image_class)):
        image_path = os.path.join(data_dir, image_class, image)
        try:
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path)
            if tip not in image_exts:
                print('Image not in ext list {}'.format(image_path))
                os.remove(image_path)
        except Exception as e:
            print('Issue with image {}'.format(image_path))

data = tf.keras.utils.image_dataset_from_directory(data_dir, batch_size=32)

data_iterator = data.as_numpy_iterator()
batch = data_iterator.next()

fig, ax = plt.subplots(ncols=4, figsize=(20,20))
for idx, img in enumerate(batch[0][:4]):
    ax[idx].imshow(img.astype(int))
    ax[idx].title.set_text(batch[1][idx])
#plt.show()

data = data.map(lambda x, y: (x/255, y))
data.as_numpy_iterator().next()

train_size = int(len(data)*.7)
val_size = int(len(data)*.2)
test_size = int(len(data)*.1)+1

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size+val_size).take(test_size)


# Create the model
model = Sequential()

model.add(Conv2D(16, (3,3), 1, activation='relu', input_shape=(256,256,3)))
model.add(MaxPooling2D())

model.add(Conv2D(32, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())

model.add(Conv2D(16, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#Compile the model
model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])

logdir='logs'
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)
hist = model.fit(train, epochs=20, validation_data=val, callbacks=[tensorboard_callback])

#Plot the training and validation loss
fig = plt.figure()
plt.plot(hist.history['loss'], color='teal', label='loss')
plt.plot(hist.history['val_loss'], color='orange', label='val_loss')
fig.suptitle('Loss', fontsize=20)
plt.legend(loc='upper left')
#plt.show()

#Plot the training and validation accuracy
plt.plot(hist.history['accuracy'], color='teal', label='accuracy')
plt.plot(hist.history['val_accuracy'], color='orange', label='val_accuracy')
fig.suptitle('Accuracy', fontsize=20)
plt.legend(loc="upper left")
#plt.show()

pre = Precision()
re = Recall()
acc = BinaryAccuracy()

for batch in test.as_numpy_iterator(): 
    X, y = batch
    yhat = model.predict(X)
    pre.update_state(y, yhat)
    re.update_state(y, yhat)
    acc.update_state(y, yhat)

#Print the precision, recall, and accuracy
print(f'Precision:{pre.result().numpy()}, Recall:{re.result().numpy()}, Accuracy:{acc.result().numpy()}')

img = cv2.imread(os.path.join('site','static','images','dirty.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

img = cv2.imread(os.path.join('site','static','images','dirty2.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

img = cv2.imread(os.path.join('site','static','images','dirty3.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

img = cv2.imread(os.path.join('site','static','images','dirty4.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

img = cv2.imread(os.path.join('site','static','images','dirty5.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

img = cv2.imread(os.path.join('site','static','images','clean.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

img = cv2.imread(os.path.join('site','static','images','clean2.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

img = cv2.imread(os.path.join('site','static','images','clean3.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

img = cv2.imread(os.path.join('site','static','images','clean4.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

img = cv2.imread(os.path.join('site','static','images','clean5.jpg'))
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, axis=0))
print(yhat)
if yhat > 0.5: 
    print(f'Predicted class is dirty')
else:
    print(f'Predicted class is clean')

#Save the model
model.save(os.path.join('site','models', 'streetsmodel.h5'))
new_model = load_model(os.path.join('site','models', 'streetsmodel.h5'))
yhatnew = new_model.predict(np.expand_dims(resize/255, 0))
