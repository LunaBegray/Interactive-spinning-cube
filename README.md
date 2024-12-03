# 3D Rotating Cube Visualization

This Python application visualizes a 3D rotating cube using wireframe rendering. The app includes an interactive UI built with **Tkinter** for adjusting rotation angles dynamically.

---

## Features
- **3D Wireframe Cube**: Displays a cube with points connected by lines for a clear 3D perspective.
- **Interactive Controls**: Adjust rotation angles for the X, Y, and Z axes in real-time using sliders.
- **Reset Option**: Easily reset all angles to their default values.

---

## Requirements
- Python 3.7+
- Install required libraries:
  ```bash
  pip install pillow
  ```

---

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Use the sliders to control the cube's rotation along different axes.
3. Press the **Reset** button to return all rotations to zero.

---

## Customization
- **Adjust Speed**: Modify `self.root.after(50, self.update_rotation)` for faster or slower rotation.
- **Line Styles**: Change colors or widths in `self.canvas.create_line`.

---
