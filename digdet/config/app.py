# imports - standard packages
import os

# imports - third-party packages
import cv2

# imports - module imports
from digdet.config.base import BaseConfig

class AppConfig(BaseConfig):
    MNIST_SIZE_INPUT = (28, 28)

    class Parameters(object):
        GAUSSIAN_BLUR = { "ksize": (5, 5), "sigmaX": 0 }
        THRESHOLD     = { "thresh": 90, "maxval": 255, "type": cv2.THRESH_BINARY_INV }
        FIND_CONTOURS = { "mode": cv2.RETR_EXTERNAL, "method": cv2.CHAIN_APPROX_SIMPLE }

    class Path(BaseConfig.Path):
        DATA   = os.path.join(BaseConfig.Path.ROOT, 'data')
        MODELS = os.path.join(DATA, 'models')
