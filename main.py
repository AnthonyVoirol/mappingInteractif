import cv2
import numpy as np # Import nécessaire pour la modification de vision
from camera import CameraManager
from vision import ColorTracker

def main():
    # 1. Initialisation
    cam = CameraManager()
    
    # --- NOUVELLE COULEUR : ROSE (#E8B7C7) ---
    # Teinte (H) : entre 160 et 180 (les roses/violets)
    # Saturation (S) : Assez basse car c'est un rose pastel (30 à 150)
    # Luminosité (V) : Moyenne à forte (100 à 255)
    pink_tracker = ColorTracker([160, 30, 100], [180, 150, 255])
    # ----------------------------------------
    
    # 2. Boucle principale
    while True:
        frame = cam.get_frame()
        
        if frame is not None:
            mask, frame_filtered = pink_tracker.apply_mask(frame)
            center, contour = pink_tracker.get_tracking_data(mask)
            if center is not None and contour is not None:
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                cv2.circle(frame, center, 7, (255, 255, 255), -1)
                cv2.putText(frame, f"Post-it: {center}", (center[0]+10, center[1]), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.imshow("Suivi Post-it (Original)", frame)
            cv2.imshow("Masque Noir et Blanc", mask)
            
        # 3. Condition de sortie (Appuyer sur 'q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 4. Nettoyage
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()