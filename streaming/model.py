
# coding: utf-8

# In[5]:

import sys
import time
import numpy as np
import cv2
import gluoncv as gcv
import mxnet as mx
import bounding_box
from mjpeg_client import MJPEGClient

from queue import Queue
from threading import Thread
import requests

q = Queue()

def command_loop():
    global q

    while True:
        tup = q.get()
        print(tup)
        r = requests.post(sys.argv[2], data={
            'xmin': tup[0],
            'ymin': tup[1],
            'xmax': tup[2],
            'ymax': tup[3]
        })
        #print(sent, r.text)

def start_commander():
    t = Thread(target=command_loop)
    t.daemon = True
    t.start()

def send_bbox(tup):
    q.put(tup)


def detection_loop():

    start_commander()

    net = gcv.model_zoo.get_model('ssd_512_mobilenet1.0_voc', pretrained=True)


    client = MJPEGClient(sys.argv[1])

    client.start()

    csrc = iter(client)

    while True:
        # Load frame from the camera
        frame = next(csrc)
        buf = np.fromstring(frame, np.uint8)
        img = cv2.imdecode(buf, cv2.IMREAD_COLOR)

        # Image pre-processing
        frame = mx.nd.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).astype('uint8')
        rgb_nd, frame = gcv.data.transforms.presets.ssd.transform_test(
            frame, short=512, max_size=700)

        # Run frame through network
        class_IDs, scores, bounding_boxes = net(rgb_nd)

        # Display the result
        # print(net.classes[int(class_IDs[0, 0, 0].asscalar())])

        # gcv.utils.viz.plot_bbox(frame, bounding_boxes[0], scores[0],
        #                      class_IDs[0], class_names=net.classes, )
        img, detected, bbox = bounding_box.plot_bbox(frame, bounding_boxes[0], scores[0],
                            class_IDs[0], class_names=net.classes, )

        if detected:
            #print('detected bottle')
            print(bbox)
            send_bbox(bbox)

        
        yield img


