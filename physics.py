import pymunk
import config
import numpy as np

class PhysicsEngine:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (config.GRAVITY_X, config.GRAVITY_Y)
        self.listBalls = []
        self.current_obstacle = None
        
    def spawn_ball(self):
        body = pymunk.Body()
        body.position = config.CAMERA_WIDTH // 2, 50
        poly = pymunk.Circle(body, config.BALL_RADIUS)
        poly.mass = config.BALL_MASS
        poly.elasticity = config.BALL_ELASTICITY
        self.space.add(body, poly)
        self.listBalls.append(body) 
        
    def update_obstacle(self, contour):
        if contour is None or len(contour) < 3:
            return
        
        if self.current_obstacle is not None:
            old_body, old_poly = self.current_obstacle
            self.space.remove(old_body, old_poly)
        
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        points = contour.reshape(-1, 2).tolist()
        poly = pymunk.Poly(body, points)
        self.current_obstacle = (body, poly)
        self.space.add(body, poly)

    def step(self):
        self.space.step(1.0 / config.FPS)
        
    def get_balls_positions(self):
        positions = []
        for body in self.listBalls:
            positions.append((int(body.position.x), int(body.position.y)))
        return positions