import cv2
from PIL import ImageGrab
import numpy as np

def screen_record():
    screen_width, screen_height = ImageGrab.grab().size
    fourcc = cv2.VideoWriter_fourcc("m","p","4","v")
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (screen_width, screen_height))


    while True:
        img = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow('Video capture', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    # out.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    screen_record()

