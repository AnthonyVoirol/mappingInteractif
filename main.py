import cv2
import numpy as np
import pygame
import config
from camera import CameraManager
from vision import ColorTracker
from physics import PhysicsEngine
from renderer import PygameRenderer

def main():
    # 1. Initialisation
    cpt = 0
    cam = CameraManager()
    engine = PhysicsEngine()
    renderer = PygameRenderer()
    
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
            tracking_data = pink_tracker.get_tracking_data(mask)
            contours_only = [data[1] for data in tracking_data]
            engine.update_obstacles(contours_only)

            for center, contour in tracking_data:
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                cv2.circle(frame, center, 7, (255, 255, 255), -1)
                cv2.putText(frame, f"Post-it: {center}", (center[0]+10, center[1]), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                
            positions = engine.get_balls_positions()
            
            renderer.clear_screen()
            renderer.draw_balls(positions)
            renderer.update_display()
            
            for pos in positions:
                cv2.circle(frame, pos, config.BALL_RADIUS, (255, 255, 255), -1)
                
            cv2.imshow("Suivi Post-it (Original)", frame)
            #cv2.imshow("Masque Noir et Blanc", mask)
            
            engine.step()
            engine.clean_balls()
            
            if cpt % config.SPAWN_RATE == 0:
                engine.spawn_ball()
                
            cpt = cpt + 1
            
            for event in pygame.event.get():
                pass
            
        # 3. Condition de sortie (Appuyer sur 'q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 4. Nettoyage
    cam.release()
    cv2.destroyAllWindows()
    pygame.quit()

if __name__ == "__main__":
    main()