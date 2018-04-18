# Import Tensorflow
import tensorflow as tf 

sess = tf.Session()

hello = tf.constant("Hello world from tensorflow")
print(sess.run(hello))

# Performing Simple Math
a = tf.constant(20)
b = tf.constant(22)
print("a + b = {}".format(sess.run(a + b )))