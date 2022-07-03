#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
import os

import cv2
import matplotlib.pyplot as plt
import zmq
import utils as ut

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

path_im = r'C:\Users\ramon\OneDrive\Pictures'


for f in os.listdir(path_im):
    if f.endswith('.jpg'):
        path_f = os.path.join(path_im,f)

        im = cv2.imread(path_f)
        imp = ut.pack_image(im)

        socket.send(imp)
        # ip.send_zipped_pickle(socket,d)

        #  Get the reply.
        imb = socket.recv()
        imb2 = ut.unpack(imb)

        plt.imshow(imb2)
        plt.show()

        # print("Received reply %s [ %s ]" % (request, 'message'))