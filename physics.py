import pymunk
import config
import numpy as np
import cv2

class PhysicsEngine:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (config.GRAVITY_X, config.GRAVITY_Y)
        self.listBalls = []
        self.current_obstacles = []
        
    def spawn_ball(self):
        body = pymunk.Body()
        body.position = config.CAMERA_WIDTH // 2, 50
        poly = pymunk.Circle(body, config.BALL_RADIUS)
        poly.mass = config.BALL_MASS
        poly.elasticity = config.BALL_ELASTICITY
        self.space.add(body, poly)
        self.listBalls.append(body) 
        
    def update_obstacles(self, contours_list):       
        for body, poly in self.current_obstacles:
            self.space.remove(body, poly)
        self.current_obstacles.clear()

        for contour in contours_list:
            if contour is None or len(contour) < 3:
                continue
            
            hull = cv2.convexHull(contour)
            epsilon = 0.02 * cv2.arcLength(hull, True)
            approx_poly = cv2.approxPolyDP(hull, epsilon, True)
            
            if len(approx_poly) < 3:
                continue
            
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            points = approx_poly.reshape(-1, 2).tolist()
            poly = pymunk.Poly(body, points)
            poly.elasticity = config.BALL_ELASTICITY
            self.space.add(body, poly)
            self.current_obstacles.append((body, poly))

    def step(self):
        self.space.step(1.0 / config.FPS)
        
    def get_balls_positions(self):
        positions = []
        for body in self.listBalls:
            positions.append((int(body.position.x), int(body.position.y)))
        return positions