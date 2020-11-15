import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import src.core.dataAdapter as adapter
import src.core.network as net
import matplotlib.pyplot as plt
# 데이터 셔플이 필요시 주석 제거
#import src.tool.fileclassification as fileclass


model = net.loadModel()
train_x, train_y, test_x, test_y = adapter.loadMemory()
ret = model.fit(train_x, train_y, epochs=100, verbose=2)
loss = ret.history['loss']
plt.plot(loss)
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

test_loss, test_acc = model.evaluate(test_x,  test_y, verbose=2)
print(test_acc)
net.saveModel(model)