model = loadModel()
tx, ty, x, y = loadMemory()
ret = model.fit(train_x, train_y, epochs=100, verbose=2)

saveModel(model)