import cv2
import numpy as np
import config

class Calibrator:
    def __init__(self):
        self.matrix = None

    def compute_matrix(self, camera_points):
        src_points = np.array(camera_points, dtype=np.float32)
       # Ordre : Haut-Gauche, Haut-Droit, Bas-Droit, Bas-Gauche
        screen_points = [
            [0, 0],                                      # Haut-Gauche
            [config.SCREEN_WIDTH, 0],                    # Haut-Droit
            [config.SCREEN_WIDTH, config.SCREEN_HEIGHT], # Bas-Droit
            [0, config.SCREEN_HEIGHT]                    # Bas-Gauche
        ]
        
        dst_points = np.array(screen_points, dtype=np.float32)
        self.matrix, _ = cv2.findHomography(src_points, dst_points)
        
        print("Matrice de calibration calculée avec succès !")