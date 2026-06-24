# GestureCanvas

GestureCanvas is a real-time computer vision-based virtual drawing system that enables users to draw in the air using hand gestures. It uses MediaPipe for real-time hand landmark detection and OpenCV for rendering a virtual canvas. The system tracks the index finger movement and converts it into smooth digital strokes displayed on screen.

---

## Features

- Real-time hand tracking using webcam
- 21 hand landmark detection using MediaPipe
- Air drawing using index finger movement
- Smooth stroke rendering on virtual canvas
- Lightweight and CPU-efficient system
- Modular and extensible architecture
- No external hardware required

---

## Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy

---

## Project Structure
```
gesture-canvas/
├── src/
│   ├── __init__.py
│   ├── hand_tracker.py
│   ├── canvas.py
│   ├── utils.py
├── app.py
├── requirements.txt
└── README.md
```
---

## Installation

### Clone the repository
```
git clone https://github.com/samoff04/GestureCanvas.git
cd GestureCanvas
```
### Create virtual environment
```
python -m venv venv
venv\Scripts\activate
```
### Install dependencies
```
pip install -r requirements.txt
```
---

## How to Run
```
python app.py
```
---

## Controls

- Move index finger → Draw on canvas
- Press Q → Quit application

---

## Working Principle

- Webcam captures real-time video frames
- MediaPipe detects hand landmarks
- Index finger tip (landmark 8) is tracked
- Movement is converted into (x, y) coordinates
- OpenCV draws lines between consecutive points
- Canvas is overlaid on live video feed

---

## Future Improvements

- Gesture-based color switching
- Eraser mode using fist gesture
- Open palm gesture to clear canvas
- Shape drawing (circle, rectangle)
- Save canvas as image (PNG/JPG)
- Handwriting recognition (OCR integration)
- UI overlay controls for tools

---

## Use Cases

- Virtual whiteboard systems
- Touchless drawing applications
- Human-computer interaction systems
- Gesture-controlled interfaces

---

## Troubleshooting

Camera not opening:
cv2.VideoCapture(0, cv2.CAP_DSHOW)

Low FPS:
Reduce webcam resolution or close background apps

Module errors:
pip install -r requirements.txt

---

## Author

Samarth Varshney