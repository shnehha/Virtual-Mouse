import mediapipe as mp
import cv2
import time
import pyautogui

# capturing the videocam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# initiating mediapipe
mpHands = mp.solutions.hands
hands_detector = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# pyautogui method to get screen height and width
screen_width, screen_height = pyautogui.size()
index_y = 0
pTime = 0
cTime = 0

# reading the frame
while True:
    res, frame = cap.read()
    frame = cv2.flip(frame, 1)                           # to make the cursor and finger move in the same direction
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_height, frame_width, _ = frame.shape
    result = hands_detector.process(frameRGB)
    hands = result.multi_hand_landmarks
    if hands:
        for hand in hands:
            mpDraw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)
            for id, landmark in enumerate(hand.landmark):
                x = int(landmark.x * frame_width)                          # to get the position in respect to screen
                y = int(landmark.y * frame_height)
                if id == 8:                                                # index finger
                    cv2.circle(img=frame, center=(x, y), radius=25, color=(255, 255, 255), thickness=2)
                    cv2.circle(img=frame, center=(x, y), radius=17, color=(130, 0, 75), thickness=3)

                    index_x = int(screen_width / frame_width * x)          # position of fingers in respect to screen
                    index_y = int(screen_height / frame_height * y)
                    pyautogui.moveTo(index_x, index_y)                     # function to move cursor

                if id == 4:                                                # thumb
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(255, 255, 255), thickness=2)
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(225, 76, 185), thickness=2)

                    thumb_x = int(screen_width / frame_width * x)          # position of fingers in respect to screen
                    thumb_y = int(screen_height / frame_height * y)
                    print('max', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 50:
                        pyautogui.click()                                  # function to click

                if id == 12:                                               # middle finger
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(255, 255, 255), thickness=2)
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(225, 76, 185), thickness=1)

                    right_x = (screen_width/frame_width * x)               # position of fingers in respect to screen
                    right_y = (screen_height/frame_height * y)
                    print('min', abs(index_y - right_y))
                    if abs(index_y - right_y) < 8:
                        pyautogui.rightClick()                             # function to click

                if id == 5:                                                # index finger mcp
                    cv2.circle(img=frame, center=(x, y), radius=25, color=(255, 255, 255), thickness=3)
                    cv2.circle(img=frame, center=(x, y), radius=17, color=(130, 0, 75), thickness=2)

                    index_mcp_x = int(screen_width / frame_width * x)      # position of fingers in respect to screen
                    index_mcp_y = int(screen_height / frame_height * y)
                    if abs(index_y - index_mcp_y) < 10:
                     pyautogui.scroll(-100, index_mcp_x, index_mcp_y)      # function to scroll down

                if id == 20:                                               # pinky finger
                    cv2.circle(img=frame, center=(x, y), radius=25, color=(255, 255, 255), thickness=3)
                    cv2.circle(img=frame, center=(x, y), radius=17, color=(130, 0, 75), thickness=2)

                    pinky_x = int(screen_width / frame_width * x)          # position of fingers in respect to screen
                    pinky_y = int(screen_height / frame_height * y)
                    if abs(index_y - pinky_y) < 20:
                     pyautogui.scroll(100, pinky_x, pinky_y)               # function to scroll up

    # Frame rate
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'FPS: ' + str(fps), (3, 35), font, 0.8, (130, 0, 75), 2)
    cv2.imshow('control window', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()