import functools
import os

from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
# import tensorflow_hub as hub

print("TF Version: ", tf.__version__)
# print("TF Hub version: ", hub.__version__)
print("Eager mode enabled: ", tf.executing_eagerly()) # What's eager mode?
print(f"GPU available: {tf.config.list_physical_devices('GPU')}")

# Define image loading and visualization functions  { display-mode: "form" }

def crop_center(image):
    """Returns a cropped square image."""
    shape = image.shape
    print(f"image shape: {shape}")
    new_shape = min(shape[1], shape[2])
    offset_y = max(shape[1] - shape[2], 0) // 2
    offset_x = max(shape[2] - shape[1], 0) // 2
    image = tf.image.crop_to_bounding_box(
        image, offset_y, offset_x, new_shape, new_shape)
    return image

# functools: https://docs.python.org/3/library/functools.html
# If maxsize is set to None, the LRU feature is disabled and the cache can grow without bound.
@functools.lru_cache(maxsize=None) 
def load_image(image_url, image_size=(256,256), preserve_aspect_ratio=True):
    """Loads and preprocesses images."""
    # Cache image file locally.
    image_path = tf.keras.utils.get_file(os.path.basename(image_url)[-128:], image_url)
    # Load and convert to float32 numpy array, add batch dimension, and normalize to range [0, 1].
    
