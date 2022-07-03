import image_processing as ip
import pickle
import zlib
import numpy as np

def pack_image(im):
    sz = im.shape
    imr = ip.im2bytearray(im)
    d = dict()
    d.setdefault('imr', imr)
    d.setdefault('size', sz)
    p = pickle.dumps(d, pickle.HIGHEST_PROTOCOL)
    z = zlib.compress(p)
    return z


def unpack(z):

    p = zlib.decompress(z)
    d = pickle.loads(p)
    sz = d.get('size')
    imr = d.get('imr')
    channels = 1
    if len(sz) == 3:
        channels = sz[2]
    # reconstruct image
    im_int = ip.bytearray2im(imr,channels)
    im = np.resize(im_int, sz)
    return im