import cv2
import config  # On importe ton fichier config.py

class CameraManager:
    def __init__(self):
        # On utilise les variables définies dans config.py
        self.url = config.CAMERA_URL
        self.cap = cv2.VideoCapture(self.url)
        
        # On peut aussi définir la résolution via la config
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)

    def get_frame(self):
        # On lit une image du flux
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        # Toujours libérer la caméra quand on a fini
        self.cap.release()