import cv2
import numpy as np
import pygame
import config
from camera import CameraManager
from vision import ColorTracker
from physics import PhysicsEngine
from renderer import PygameRenderer
from calibration import Calibrator

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clic détecté : {x}, {y}")
        param.append((x, y))

def main():
    is_calibrating = True
    points_calibration = []
    cpt = 0
    
    cam = CameraManager()
    engine = PhysicsEngine()
    renderer = PygameRenderer()
    calibrator = Calibrator() 
    
    pink_tracker = ColorTracker([140, 10, 150], [180, 255, 255])

    cv2.namedWindow("Suivi Post-it (Original)")
    cv2.setMouseCallback("Suivi Post-it (Original)", mouse_callback, param=points_calibration)
    
    while True:
        frame = cam.get_frame()
            
        if frame is not None:
            mask, frame_filtered = pink_tracker.apply_mask(frame)
            tracking_data = pink_tracker.get_tracking_data(mask)
            contours_only = [data[1] for data in tracking_data]

            for center, contour in tracking_data:
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                cv2.circle(frame, center, 7, (255, 255, 255), -1)
                cv2.putText(frame, f"Post-it: {center}", (center[0]+10, center[1]), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
            if is_calibrating and len(points_calibration) >= 4:
                calibrator.compute_matrix(points_calibration)
                is_calibrating = False 
            
            if is_calibrating:
                renderer.clear_screen()
                renderer.draw_calibration_pattern()
                renderer.update_display()
                
                for i, pt in enumerate(points_calibration):
                    cv2.circle(frame, pt, 5, (0, 0, 255), -1)
                    cv2.putText(frame, f"P{i+1}", (pt[0]+10, pt[1]-10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    
                cv2.putText(frame, f"Calibration: {len(points_calibration)}/4 clics (Haut-Gauche, Haut-Droit, Bas-Droit, Bas-Gauche)", 
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                
            else:
                if calibrator.matrix is not None:
                    transformed_contours = []
                    for contour in contours_only:
                        contour_float = np.array(contour, dtype=np.float32)
                        contour_transformed = cv2.perspectiveTransform(contour_float, calibrator.matrix)
                        transformed_contours.append(np.int32(contour_transformed))
                    engine.update_obstacles(transformed_contours)

                positions = engine.get_balls_positions()
                
                renderer.clear_screen()
                renderer.draw_balls(positions)
                renderer.update_display()
                
                for pos in positions:
                    cv2.circle(frame, pos, config.BALL_RADIUS, (255, 255, 255), -1)
                
                engine.step()
                engine.clean_balls()
                
                if cpt % config.SPAWN_RATE == 0:
                    engine.spawn_ball()
                    
                cpt += 1
                
            cv2.imshow("Suivi Post-it (Original)", frame)
            
            for event in pygame.event.get():
                pass
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    pygame.quit()

if __name__ == "__main__":
    main()