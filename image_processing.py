from cv2 import cvtColor, COLOR_BGR2GRAY, INTER_AREA, resize, imencode, imdecode, IMREAD_COLOR, IMREAD_GRAYSCALE
import numpy as np

def process(img):
    gray = cvtColor(img, COLOR_BGR2GRAY)
    red = resize(gray, (200,200),interpolation = INTER_AREA)
    return red

def im2bytearray(img):
    return imencode('.jpg', img)[1].tostring()

def bytearray2im(imbyte, channels = 3):
    nparr = np.fromstring(imbyte, np.uint8)
    if channels == 3:
        img = imdecode(nparr, IMREAD_COLOR)
    else:
        img = imdecode(nparr, IMREAD_GRAYSCALE)

    return img

def bytearray2im2(imbyte):
    nparr = np.fromstring(imbyte, np.uint8)
    r = np.resize(nparr, ( 3264,2448, 3))
    # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return r

import pickle
import zlib


def send_zipped_pickle(socket, obj, flags=0, protocol=pickle.HIGHEST_PROTOCOL):
    """pickle an object, and zip the pickle before sending it"""
    p = pickle.dumps(obj, protocol)
    z = zlib.compress(p)
    return socket.send(z, flags=flags)


def recv_zipped_pickle(socket, flags=0):
    """inverse of send_zipped_pickle"""
    z = socket.recv()
    p = zlib.decompress(z)
    return pickle.loads(p)