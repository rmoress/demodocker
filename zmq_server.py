#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import matplotlib.pyplot as plt
import zmq

import image_processing as ip
import utils as ut

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    z = socket.recv()
    print('message recived on server...')
    im = ut.unpack(z)
    # plt.imshow(im)
    # plt.title('input image')
    # plt.show()
    #do something
    imp = ip.process(im)
    # plt.imshow(imp)
    # plt.title('image processed')
    # plt.show()

    #pack back
    p = ut.pack_image(imp)

    #  Send reply back to client
    socket.send(p)