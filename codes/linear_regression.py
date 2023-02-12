# 导入 TensorFlow 库并命名为 tf
import tensorflow as tf

# 创建训练数据；即 x_train 和 y_train
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# 构建模型；使用 tf.keras.Sequential 创建模型
model = tf.keras.Sequential()
# 构建模型；使用 model.add 添加一个密集层，该层有 1 个单元并且输入形状为 1
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

# 编译模型；model.compile 定义优化器、损失函数以及评估指标。
model.compile(optimizer=tf.keras.optimizers.SGD(0.01), loss='mean_squared_error')

# 训练模型；model.fit 训练模型，并运行 500 个
model.fit(x_train, y_train, epochs=500)

# 预测结果
print(model.predict([10.0]))
