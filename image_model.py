import pandas as pd
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_path = "data/images/train"

# สร้าง dataframe จากชื่อไฟล์
files = os.listdir(train_path)
data = []

for file in files:
    if "dog" in file.lower():
        label = "dog"
    elif "cat" in file.lower():
        label = "cat"
    else:
        continue
    data.append([file, label])

df = pd.DataFrame(data, columns=["filename", "class"])

# generator
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_gen = datagen.flow_from_dataframe(
    df,
    directory=train_path,
    x_col="filename",
    y_col="class",
    target_size=(128,128),
    class_mode="binary",
    subset="training"
)

val_gen = datagen.flow_from_dataframe(
    df,
    directory=train_path,
    x_col="filename",
    y_col="class",
    target_size=(128,128),
    class_mode="binary",
    subset="validation"
)

# CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# train
model.fit(train_gen, validation_data=val_gen, epochs=5)

# save
model.save("image_model.keras")

print("CNN model trained and saved")