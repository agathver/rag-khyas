import cv2
import numpy as np
import mxnet as mx

def plot_bbox(img, bboxes, scores=None, labels=None, thresh=0.5,
              class_names=None, colors=None, ax=None,
              reverse_rgb=False, absolute_coordinates=True):
    
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    bbox = None
    detected = False

    if labels is not None and not len(bboxes) == len(labels):
        raise ValueError('The length of labels and bboxes mismatch, {} vs {}'
                         .format(len(labels), len(bboxes)))
    if scores is not None and not len(bboxes) == len(scores):
        raise ValueError('The length of scores and bboxes mismatch, {} vs {}'
                         .format(len(scores), len(bboxes)))

    # ax = plot_image(img, ax=ax, reverse_rgb=reverse_rgb)

    if len(bboxes) < 1:
        return

    if isinstance(bboxes, mx.nd.NDArray):
        bboxes = bboxes.asnumpy()
    if isinstance(labels, mx.nd.NDArray):
        labels = labels.asnumpy()
    if isinstance(scores, mx.nd.NDArray):
        scores = scores.asnumpy()

    if not absolute_coordinates:
        # convert to absolute coordinates using image shape
        height = img.shape[0]
        width = img.shape[1]
        bboxes[:, (0, 2)] *= width
        bboxes[:, (1, 3)] *= height

    # use random colors if None is provided
    if colors is None:
        colors = dict()
    for i, bbox in enumerate(bboxes):
        if scores is not None and scores.flat[i] < thresh:
            continue
        if labels is not None and labels.flat[i] < 0:
            continue
        
        cls_id = int(labels.flat[i]) if labels is not None else -1
        
        if class_names is not None and cls_id < len(class_names):
            class_name = class_names[cls_id]
        else:
            class_name = str(cls_id) if cls_id >= 0 else ''

        #print(class_name, xmin, ymin, xmax, ymax)

        score = '{:.3f}'.format(scores.flat[i]) if scores is not None else ''
        
        font = cv2.FONT_HERSHEY_SIMPLEX

        if class_name in ['bottle', 'cup']:
            detected = True

            xmin, ymin, xmax, ymax = [int(x) for x in bbox]

            bbox = (xmin, ymin, xmax, ymax)

            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255,255,255), 3)

            text = '{:s} {:s}'.format(class_name, score)
            cv2.putText(img, text,(xmin, ymin - 2,), font, 1,(255,255,255),2,cv2.LINE_AA)

    return (img, detected, bbox)