import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import src.core.dataAdapter as adapter
import src.core.network as net
import src.core.fileclassification as fileclass

import matplotlib.pyplot as plt

from tensorflow.keras.callbacks import TensorBoard
from datetime import datetime

# 새로운 이미지 셋을 학습하길 원할 경우 주석을 풀어야한다.
fileclass.setup_image_data()

model = net.loadModel()
train_x, train_y, test_x, test_y, test_names = adapter.loadMemory()
ret = model.fit(train_x, train_y, epochs=100, verbose=1)

loss = ret.history['loss']
plt.plot(loss)
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()


test_acc = model.evaluate(test_x, test_y, verbose=2)
print(test_acc)
net.saveModel(model)


# tensorboard = TensorBoard(log_dir='../logs/{}'.format(datetime.now().strftime("%Y%m%d-%H%M%S")))
# ret = model.fit(train_x, train_y, epochs=2, verbose=1, callbacks=[tensorboard])