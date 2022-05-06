import tensorflow as tf

print("Tensorflow version: " + tf.__version__)

def run_tut():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test/ 255.0 # 0~1

    model = tf.keras.models.Sequential([
        
    ])

# build a ML model by stacking layers

if __name__ == "__main__":
    run_tut()