import cv2
from threading import Thread
import queue

class RTCamera(Thread):

    def run(self) -> None:
        while True:
            flag, img = self._cap.read()

            if flag:
                pass

    def start(self, id) -> None:
        self._cap = cv2.VideoCapture(id)
        self._imgQ = queue.Queue()

    def __init__(self):
        Thread.__init__()

        self.daemon = True


if __name__ == '__main__':
    print('test')
