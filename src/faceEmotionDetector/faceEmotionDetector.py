# https://github.com/atulapra/Emotion-detection
import numpy as np
import cv2

from datetime import datetime
import os

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from multiprocessing import Queue

class FaceEmotionDetector:
    def __init__(self):
        super().__init__()
        # Create the model
        self.model = Sequential([
            Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)),
            Conv2D(64, kernel_size=(3, 3), activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Dropout(0.25),

            Conv2D(128, kernel_size=(3, 3), activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(128, kernel_size=(3, 3), activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Dropout(0.25),

            Flatten(),
            Dense(1024, activation='relu'),
            Dropout(0.5),
            Dense(7, activation='softmax')
        ])

        current_path = os.getcwd()
        self.model.load_weights(os.path.join(current_path, 'faceEmotionDetector\\resources\\model.h5'))

        # dictionary which assigns each label an emotion (alphabetical order)
        self.emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

        self.facecasc = cv2.CascadeClassifier(os.path.join(current_path, 'faceEmotionDetector\\resources\\haarcascade_frontalface_default.xml'))

    def detect(self, frame):
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            faces = self.facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)
            results = []

            for (x, y, w, h) in faces:
                # initialize rectangle
                cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]

                # predict current emotion
                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                prediction = self.model.predict(cropped_img)
                maxindex = int(np.argmax(prediction))
                emotion = self.emotion_dict[maxindex]

                # show rectangle and emotion in opencv frame
                cv2.putText(frame, emotion, (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                results.append([str(datetime.now().timestamp()), str(emotion)])

            return results

# if __name__ == "__main__":
#     emotions_q = Queue(5)
#     detector = FaceEmotionDetector(emotions_q)
#     # start the webcam feed
#     cap = cv2.VideoCapture(0)
#     while True:
#         # Find haar cascade to draw bounding box around face
#         ret, frame = cap.read()
#         if not ret:
#             break

#         detector.detect(frame)
#         cv2.imshow('Video', cv2.resize(frame,(1600,960),interpolation = cv2.INTER_CUBIC))
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
