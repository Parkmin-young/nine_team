import tensorflow as tf
import os
"""
1. 모델 생성(model.h5 가 없는 경우)
2. 모델 로딩(model.h5 가 있는 경우)
3. loadModel() : tensorflow.keras.model.Model 제공
4. saveModel(model : tensorflow.keras.model.Model) 제공
"""

SAVED_MODEL_PATH = os.path.dirname(__file__)+ "/model" # 경로 중 디렉토리명만 얻고 model 폴더 설정

def loadModel():
    # 반환값 정의
    model : tf.keras.Model
    try:
        model = tf.keras.models.load_model(SAVED_MODEL_PATH)
    except Exception as identifier:
        # TODO 모델이 없는 경우
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Conv2D(filters=5, kernel_size=(3, 3), activation="relu"))
        model.add(tf.keras.layers.Conv2D(filters=10, kernel_size=(3, 3), activation="relu"))
        model.add(tf.keras.layers.Conv2D(filters=20, kernel_size=(3, 3), activation="relu"))
        model.add(tf.keras.layers.Conv2D(filters=30, kernel_size=(3, 3), activation="relu"))
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(1, activation="sigmoid"))
        model.build((1,512,512,3))
        model.compile(optimizer="adam", loss="binary_crossentropy")
    
    return model

def saveModel(model: tf.keras.Model): # 모델 저장
    model.save(SAVED_MODEL_PATH)

if __name__ == "__main__":
    model = loadModel()
    print(model.summary())
