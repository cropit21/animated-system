import threading
import numpy
import opennsfw2
from PIL import Image
from keras import Model

from roop.typing import Frame

PREDICTOR = None
THREAD_LOCK = threading.Lock()
MAX_PROBABILITY = 0.85


def get_predictor() -> Model:
    # Mengembalikan None atau model kosong untuk menonaktifkan prediktor
    return None


def clear_predictor() -> None:
    global PREDICTOR

    PREDICTOR = None


def predict_frame(target_frame: Frame) -> bool:
    # Langsung mengembalikan False, artinya frame tidak dianggap NSFW
    return False


def predict_image(target_path: str) -> bool:
    # Langsung mengembalikan False, artinya gambar tidak dianggap NSFW
    return False


def predict_video(target_path: str) -> bool:
    # Langsung mengembalikan False, artinya video tidak dianggap NSFW
    return False
