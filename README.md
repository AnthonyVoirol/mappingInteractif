# Real-Time Interactive Projection Mapping

## Description
This project is an interactive projection mapping application built in Python. It bridges the physical and digital worlds by using computer vision to track real-world objects (such as colored markers or Post-its) on a physical surface. A 2D physics engine simulates virtual objects interacting with these physical obstacles, and the output is projected back onto the surface in real-time, creating a seamless mixed-reality experience.

## How It Works (Architecture)
The system operates on a continuous pipeline across four main components:

1. **Vision & Tracking (OpenCV):** A camera captures the projection surface. The video feed is processed using HSV color space thresholding to isolate and track specific physical markers dynamically.
2. **Spatial Calibration (Homography):** Because the camera and projector have different resolutions, aspect ratios, and physical perspectives, the system uses a 4-point manual calibration. OpenCV computes a homography matrix to warp and translate the camera's coordinate system into the projector's exact coordinate space.
3. **Physics Simulation (Pymunk):** The aligned coordinates of the physical markers are converted into static rigid bodies within a 2D physics space. Virtual objects (e.g., falling balls) are spawned as dynamic bodies that calculate collisions and gravity against the static physical obstacles.
4. **Rendering (Pygame):** The engine renders the virtual objects as high-contrast shapes (white on a black background). When projected, the black background emits no light, leaving only the virtual objects visible on the physical wall.

## Built With
* Python 3.13
* OpenCV - Real-time computer vision and contour extraction.
* Pymunk - 2D rigid body physics simulation.
* Pygame - Fullscreen graphics rendering.
* Numpy - Matrix operations and homography calculations.

## Prerequisites & Hardware
* A camera (e.g., webcam or smartphone connected via Windows Phone Link).
* A video projector configured as a secondary monitor (Extended Display).
* A physical surface with brightly colored markers (e.g., pink Post-its).

## Installation
1. Clone the repository or download the source files.
2. Open a terminal in the project directory and create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   * **Windows:** `venv\Scripts\activate`
   * **Mac/Linux:** `source venv/bin/activate`
4. Install the required dependencies:
   ```bash
   pip install opencv-python pygame pymunk numpy
   ```

## Usage
1. Setup your hardware: connect the camera and turn on the projector. Ensure the projector is set as an extended display.
2. Adjust `CAMERA_URL`, `SCREEN_WIDTH`, and `SCREEN_HEIGHT` in `config.py` to match your specific hardware resolution (e.g., 1024x768 for older projectors).
3. Run the application:
   ```bash
   python main.py
   ```
4. **Calibration Phase:**
   * A red bounding box will be projected onto the wall.
   * On your computer monitor, view the OpenCV camera feed.
   * Click exactly on the 4 corners of the projected red box in the video feed in the following order: Top-Left, Top-Right, Bottom-Right, Bottom-Left.
5. **Interactive Phase:** Once calibrated, the physics simulation will start. Place your physical markers on the wall to see the virtual objects bounce off them.
6. Press the `q` key on the OpenCV window to safely terminate the process and close the physics engine.

## Future Improvements
* Dynamic adjustment UI for HSV thresholds to compensate for projector blooming.
* Implementation of game mechanics (goals, scoring system).
* Automatic ArUco marker calibration to replace manual 4-point clicking.