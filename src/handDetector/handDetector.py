
from multiprocessing import Queue
from PyQt5.QtCore import QThread
import handDetector.utils.detector_utils as detector_utils
import tensorflow as tf
import cv2
from datetime import datetime

class HandDetector(QThread):
  # Create a worker thread that loads graph and
  # does detection on images in an input queue and puts it on an output queue
  def __init__(self, height, width):
    super().__init__()
    self.frame_processed = 0
    self.score_thresh = 0.2

    self.height = height
    self.width = width
    self.num_hands = 2

  def detect(self, frame):
    if (frame is not None):
        # Actual detection. Variable boxes contains the bounding box cordinates for hands detected,
        # while scores contains the confidence for each of these boxes.
        # Hint: If len(boxes) > 1 , you may assume you have found atleast one hand (within your score threshold)

        boxes, scores = detector_utils.detect_objects(
            frame, self.detection_graph, self.sess)
        self.frame_processed += 1

        results = []
        for i in range(self.num_hands):
            if (scores[i] > self.score_thresh):
                (left, right, top, bottom) = (boxes[i][1] * self.width, boxes[i][3] * self.width,
                                              boxes[i][0] * self.height, boxes[i][2] * self.height)
                # draw bounding boxes
                p1 = (int(left), int(top))
                p2 = (int(right), int(bottom))
                cv2.rectangle(frame, p1, p2, (77, 255, 9), 3, 1)

                # return data
                x = int(left + ((right - left)/2))
                y = int(bottom + ((top - bottom) / 2))
                results.append([str(datetime.now().timestamp()), str(x), str(y)])
        return results

  def __enter__(self):
    self.detection_graph, self.sess = detector_utils.load_inference_graph()
    # self.start()
    return self

  def __exit__(self, type, value, traceback):
    # self.stop()
    self.sess.close()
    print("Handdetector closed")

  # def run(self):
  #     print(">> loading frozen model for worker")
  #     detection_graph, sess = detector_utils.load_inference_graph()
  #     self.running = True
  #     with tf.compat.v1.Session(graph=detection_graph) as sess:
  #       while self.running:
  #           #print("> ===== in worker loop, frame ", frame_processed)
  #           frame = self.input_q.get()
  #           if (frame is not None):
  #               # Actual detection. Variable boxes contains the bounding box cordinates for hands detected,
  #               # while scores contains the confidence for each of these boxes.
  #               # Hint: If len(boxes) > 1 , you may assume you have found atleast one hand (within your score threshold)

  #               boxes, scores = detector_utils.detect_objects(
  #                   frame, detection_graph, sess)
  #               # draw bounding boxes
  #               detector_utils.draw_box_on_image(
  #                   self.num_hands, self.score_thresh,
  #                   scores, boxes, self.width, self.height,
  #                   frame)

  #               detector_utils.store_hand_positions(
  #                   self.num_hands, self.score_thresh,
  #                   scores, boxes, self.width, self.height,
  #                   self.csv_q
  #               )
  #               # add frame annotated with bounding box to queue
  #               self.output_q.put(frame)
  #               self.frame_processed += 1
  #           else:
  #               self.output_q.put(frame)

  # def stop(self):
  #   self.running = False
