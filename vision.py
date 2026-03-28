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
        Trouve le plus grand contour et retourne ses coordonnées.
        """
        if mask is None:
            return None, None

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            
            if cv2.contourArea(largest_contour) > 500:
                M = cv2.moments(largest_contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    return (cX, cY), largest_contour
        
        return None, None
        