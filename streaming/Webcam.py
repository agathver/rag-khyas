
# coding: utf-8

# In[5]:

import sys
import time
import numpy as np
import cv2
import gluoncv as gcv
from matplotlib import pyplot as plt
from matplotlib import rcParams
import mxnet as mx

from mjpeg_client import MJPEGClient
from bounding_box import plot_bbox

rcParams['figure.figsize'] = 10, 10


net = gcv.model_zoo.get_model('ssd_512_mobilenet1.0_voc', pretrained=True)


client = MJPEGClient(sys.argv[1])

client.start()

csrc = iter(client)

axes = None

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
    print(net.classes[int(class_IDs[0, 0, 0].asscalar())])

    plot_bbox(img, bounding_boxes[0], scores[0],
                         class_IDs[0], class_names=net.classes, )

    cv2.imshow("test", img)
    cv2.waitKey(1)
