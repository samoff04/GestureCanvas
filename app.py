import cv2
from src.hand_tracker import get_index_finger
from src.canvas import create_canvas, draw_line
from src.utils import overlay

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
canvas = create_canvas(frame.shape)

prev_point = None
color = (0, 255, 0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, point = get_index_finger(frame)

    if prev_point and point:
        canvas = draw_line(canvas, prev_point, point, color)

    prev_point = point

    output = overlay(frame, canvas)

    cv2.imshow("GestureCanvas AI", output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()