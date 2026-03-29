# Real-Time Interactive Projection Mapping

## 📝 About The Project
This project is an interactive projection mapping application built in Python. It uses computer vision to detect physical objects (like brightly colored Post-its) on a wall in real-time. A 2D physics engine then simulates virtual balls falling and bouncing off these real-world obstacles, and the result is projected back onto the wall to create a mixed-reality experience.

## 🛠️ Built With
* **Python 3.13**
* **OpenCV** - For real-time computer vision and color tracking.
* **Pymunk** - For the 2D rigid body physics simulation.
* **Pygame** - For rendering the graphics sent to the projector.
* **Numpy** - For matrix and array mathematical operations.

## ⚙️ Prerequisites & Hardware
* A webcam or smartphone connected as a webcam (e.g., using Windows Phone Link).
* A video projector (configured as a secondary monitor).
* Python 3.10 or higher.

## 🚀 Installation
1. Clone the repository or download the project files.
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

## 🎮 How to Use
1. Ensure your camera is connected and your projector is turned on.
2. Adjust the `CAMERA_URL`, `SCREEN_WIDTH`, and `SCREEN_HEIGHT` in `config.py` to match your hardware setup.
3. Run the main script:
   ```bash
   python main.py
   ```
4. Place physical markers (e.g., pink Post-its) on the projected surface.
5. Press the `q` key on the OpenCV window to cleanly exit the application.

## 📋 To-Do List (Next Steps)
- [ ] **Camera-to-Projector Calibration:** Implement a homography matrix to align the camera's perspective (16:9) with the projector's output (4:3 native).
- [ ] **Calibration Mode:** Add a UI state to capture 4 corner points via mouse clicks for dynamic perspective warping.
- [ ] **Lighting Adjustment:** Fine-tune HSV tracking thresholds to compensate for the projector's high luminosity (ANSI Lumens) washing out the physical markers.
- [ ] **Game Design:** Add goals, dynamic spawning, or varying obstacle types.
