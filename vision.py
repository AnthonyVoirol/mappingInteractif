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
    
    def get_tracking_data(self, mask):
        """
        Trouve TOUS les contours valides et retourne une liste.
        """
        if mask is None:
            return []

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        valid_data = []
        
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    valid_data.append(((cX, cY), contour))
                    
        return valid_data
        