import cv2
from camera import CameraManager
from vision import ColorTracker

def main():
    # 1. Initialisation
    cam = CameraManager()
    blue_tracker = ColorTracker([110, 50, 50], [130, 255, 255])
    
    # 2. Boucle principale
    while True:
        frame = cam.get_frame()
        
        if frame is not None:
            mask, frame_filtered = blue_tracker.apply_mask(frame)
            # Afficher l'image dans une fenêtre nommée "Mapping"
            cv2.imshow("Original", frame)
            cv2.imshow("Masque Noir et Blanc", mask)
            cv2.imshow("Resultat Couleur", frame_filtered)
            
        # 3. Condition de sortie (Appuyer sur 'q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 4. Nettoyage
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()