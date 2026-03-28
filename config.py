# config.py

# ==========================================
# 📱 PARAMÈTRES DE LA CAMÉRA (SAMSUNG S25)
# ==========================================
# Remplace cette URL par celle donnée par l'application (ex: IP Webcam ou DroidCam)
# Si tu utilises une webcam USB classique ou DroidCam en mode USB, mets juste 0.
CAMERA_URL = 0
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

# ==========================================
# 📽️ PARAMÈTRES DU PROJECTEUR (AFFICHAGE)
# ==========================================
# Résolution de la fenêtre Pygame (idéalement la résolution de ton beamer)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60 # Images par seconde pour la boucle principale

# ==========================================
# ⚙️ PARAMÈTRES DE LA PHYSIQUE (PYMUNK)
# ==========================================
GRAVITY_X = 0
GRAVITY_Y = 900 # Plus le chiffre est grand, plus ça tombe vite
BALL_RADIUS = 15
BALL_MASS = 1.0
BALL_ELASTICITY = 0.8 # Le rebond (0 = plomb, 1 = superballe)
SPAWN_RATE = 30 # Faire apparaître une balle toutes les X frames

# ==========================================
# 🎨 COULEURS (RGB)
# ==========================================
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_DEBUG = (0, 0, 255) # Bleu pour dessiner les contours d'OpenCV