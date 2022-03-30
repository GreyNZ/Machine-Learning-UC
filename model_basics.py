# imports
import tensorflow as tf
import numpy as np

# COMMON STRIDES
# 1 or 2
# [1, 1] [2, 2]

# COMMON kernel size
# (3, 3)
# (2, 2)

# COMMON PADDING
# padding='SAME'
# padding='VALID'

# link to initializers
#https://www.tensorflow.org/api_docs/python/tf/keras/initializers/Initializer

# COMMON ACTIVATIONS
# tf.keras.layers.LeakyReLU(alpha=0.1)
#actuvation=tf.keras.activations.sigmoid(x)
#activation=tf.keras.activations.softmax(tf.random.normal(shape=(shape_here)))
#tf.keras.activations.tanh(tf.constant([-3.0,-1.0, 0.0,1.0,3.0], dtype = tf.float32))
#activation=None

# COMMON KERNEL init's
#kernel_initializer=tf.keras.initializers.Identity(gain=1.0)
#kernel_initializer=tf.keras.initializers.RandomNormal(stddev=0.1)
#kernel_initializer=initializers.RandomNormal(stddev=0.01)    # mean=0.0, stddev=0.05, seed=None
#kernel_initializer='glorot_uniform'

# COMMON BIAS
# bias_initializer=tf.keras.initializers.RandomNormal(stddev=0.1)
# bias_initializer='zeros'
# bias_initializer='ones'

# Basic Conv1D
#self.layername_rename =tf.keras.layers.Conv2D(size_here,(kernel_here), padding=padding_here, kernel_initializer=add_kernel_init_here, bias_initializer=add_bias_here, activation=activation_init_here)

# Basic MaxPool1D
#self.layername_rename =tf.keras.layers.Conv2D(size_here,(kernel_here), padding=padding_here, kernel_initializer=add_kernel_init_here, bias_initializer=add_bias_here, activation=activation_init_here)

# Basic 1D transpose
# tf.keras.layers.Conv1DTranspose(filters, kernel_size, strides=1, padding='valid', output_padding=None,activation=activation_here,kernel_initializer=add_kernel_init_here,bias_initializer=bias_init)

# Basic Conv2D
#self.layername_rename =tf.keras.layers.Conv2D(size_here,(kernel_here), padding=padding_here, kernel_initializer=add_kernel_init_here, bias_initializer=add_bias_here, activation=activation_init_here)

# Basic MaxPool 2D
#self.layername_rename =tf.keras.layers.MaxPool2D(pool_size=(poolsize_here) strides=stride_here, padding=padding_here, data_format=None)

# Basic 2D transpose
#self.layername_rename = tf.keras.layers.Conv2DTranspose(filters_here, kernel_here, strides=stride_here,padding=padding_here,kernel_initializer=add_kernel_init_here,bias_initializer=add_bias_here,activation=activation_init_here)

# Conv and Pool 3D, wont be used so just link
# https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv3D
# https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool3D



class Modelname(tf.keras.Model):
  def __init__(self):
    super(Modelname, self).__init__()
    # add layers here as needed


  def call(self, input):
    # one for each layer in model feed in order required
    # x = self.rename_me(input)
    # x = self.rename_me(x)
    # x = self.rename_me(x)
    # x = self.rename_me(x)
    # x = self.rename_me(x)
    # x = self.rename_me(x)
    # x = self.rename_me(x)
    # x = self.rename_me(x)

    return self.Modelname()
