import cv2
import numpy as np

from mjpeg_client import MJPEGClient

client = MJPEGClient('http://localhost:8080')

for frame in client:

    buf = np.fromstring(frame, np.uint8)

    img = cv2.imdecode(buf, cv2.IMREAD_COLOR)

    cv2.imshow("test", img)
    cv2.waitKey(1)