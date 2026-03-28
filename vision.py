import cv2
import numpy as np
from camera import CameraManager

class ColorTracker:
    def __init__(self, lower_color, upper_color):
        """
        Gère le traitement d'image pour détecter une couleur.
        """
        self.lower_bound = np.array(lower_color)
        self.upper_bound = np.array(upper_color)

    def apply_mask(self, frame):
        """
        Prend une image brute et retourne l'image filtrée et le masque.
        """
        if frame is None:
            return None, None
            
        # Conversion BGR vers HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Création du masque
        mask = cv2.inRange(hsv, self.lower_bound, self.upper_bound)
        
        # Application du masque sur l'image d'origine
        res = cv2.bitwise_and(frame, frame, mask=mask)
        
        return mask, res