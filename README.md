# 🏋️‍♂️ Javelin Throwing Analysis and Simulation


---

## 📌 Overview

This project offers a comprehensive system to analyze, simulate, and optimize javelin throwing techniques through two main components:

1. **🎮 Physics-Based Simulation:**  
   A GUI-based simulator that models projectile motion using real physics equations.  
   Users can adjust speed, angle, and observe the resulting throw in real time.

2. **📹 Video Analysis and Biomechanics:**  
   A vision-based tool using pose estimation and computer vision to analyze athlete movements, extract performance metrics, and assist in technique improvement.

Together, these tools aim to bridge the gap between science and sport, empowering athletes, coaches, and educators to understand and improve javelin throwing performance.

---

## 🎮 Features – Simulation Module

- **Modern PyQt5 GUI** with sliders for angle, speed, and animation speed.
- **Live Matplotlib Plot** of the javelin's trajectory.
- **Game Stats**: Displays max height, total distance, and flight time.
- **Olympic-Styled UI** with vector icons and stadium visuals.
- **Fullscreen Support** via button or `F11`.
- **Real Physics**: Uses motion equations without air resistance for educational clarity.

---

## 📹 Features – Video Analysis Module

- **Pose Estimation** using MediaPipe to extract body landmarks.
- **Angle & Velocity Analysis** based on athlete’s movement during the throw.
- **Visual Feedback** through annotated images and trajectories.
- **Targeted Technique Suggestions** based on biomechanical findings.

---

## 🔬 Scientific Background

The simulation and analysis are grounded in real-world physics and biomechanics:

### ⚙️ Physics Used in Simulation

- **Equations of Motion:**
  - \( x = v_0 \cos\theta \cdot t \)
  - \( y = v_0 \sin\theta \cdot t - \frac{1}{2}gt^2 \)
  - Range (no drag): \( R = \frac{v_0^2 \sin(2\theta)}{g} \)

- **Optimal Angle (Theory vs. Reality):**
  - Theoretical max: **45°**
  - Real-world (Olympic): **32°–36°**, due to javelin aerodynamics

- **Speeds:**
  - Elite male javelin throwers: up to **36 m/s**
  - Female athletes: **25–30 m/s**
  - World record (Men): **98.48 m** | (Women): **72.28 m**

> Note: Air resistance and lift are not included in the simulation, leading to higher distances than reality.

---

## 🧪 Real vs. Simulated Comparison

| Metric              | Real World (Olympics)       | Simulation Module                |
|---------------------|-----------------------------|----------------------------------|
| Distance Record      | 98.48 m (men) / 72.28 m     | ~100 m (no air resistance)       |
| Optimal Angle        | 32°–36°                     | Slider (30°–90°)                 |
| Release Speed        | 28–36 m/s                   | Slider (5–40 m/s)                |
| Air Drag / Lift      | Yes                         | No (for clarity/education)       |

---

## 🧰 Technologies Used

| Component             | Library/Tool       | Purpose                            |
|----------------------|--------------------|-------------------------------------|
| GUI + Simulation      | **PyQt5**           | GUI layout, sliders, buttons        |
| Plotting              | **Matplotlib**      | Live throw path visualization       |
| Physics / Math        | **NumPy**           | Trigonometry and calculations       |
| Image Handling        | **Pillow (PIL)**    | Icons and background images         |
| Video Analysis        | **OpenCV**          | Video processing, drawing           |
| Pose Estimation       | **MediaPipe**       | Detecting joints and angles         |

---

## 🖼️ Screenshots & Visuals

![Simulation Screenshot](https://github.com/Shehab-Hegab/Javelin-Throwing-Project-/assets/137138481/d6c712b7-ec57-4c54-88bc-4e5f9df45bdb)
![Pose Estimation](https://github.com/Shehab-Hegab/Javelin-Throwing-Project-/assets/137138481/324fc85e-1731-4299-9cc0-3f820f85fdc0)
![Throw Field Area](https://github.com/Shehab-Hegab/Javelin-Throwing-Project-/assets/137138481/a09d5eb4-9444-4d30-9f29-bbd3feb2b2cf)
<img width="1918" height="1078" alt="Screenshot 2025-07-10 231918" src="https://github.com/user-attachments/assets/142a846b-7493-4114-89f0-abaea56cf8c9" />


---

## 🚀 Getting Started

### ▶️ Simulation Module

1. Install Python 3.x
2. Install dependencies:
   ```bash
   pip install PyQt5 matplotlib numpy pillow
