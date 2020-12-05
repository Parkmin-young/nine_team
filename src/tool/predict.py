import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import src.core.dataAdapter as adapter
import src.core.network as net
import matplotlib.pyplot as plt
import src.core.fileclassification as fileclass

# fileclass.setup_image_data()

model = net.loadModel()
train_x, train_y, test_x, test_y, test_names = adapter.loadMemory()

ret = model.predict(test_x)

succss = 0
failed = 0
for i, data in enumerate(test_x):
    is_knu = (ret[i] > 0.5)
    is_knu_y = (test_y[i] > 0.5)
    print(test_names[i] + "는" + (is_knu and "학교로 판단됩니다." or "유사건물로 판단됩니다."))

    if is_knu_y == is_knu:
        succss += 1
    else:
        failed += 1

print("맞춘 수 : " + str(succss))
print("틀린 수 : " + str(failed))

plt.plot(ret)
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

