import cv2
import mediapipe as mp
import time
import subprocess

def PressKey(key):
    subprocess.run(["xdotool", "keydown", key])

def ReleaseKey(key):
    subprocess.run(["xdotool", "keyup", key])

right_pressed = "Right"
left_pressed = "Left"

break_key_pressed = left_pressed
accelerator_key_pressed = right_pressed

time.sleep(2.0)
current_key_pressed = set()

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5) as hands:
    while True:
        ret, image = video.read()
        if not ret:
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                h, w, c = image.shape
                for id, lm in enumerate(hand_landmark.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

        keyPressed = False
        key_pressed = None

        if len(lmList) != 0:
            fingers = []
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = fingers.count(1)

            if total == 0:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                PressKey(break_key_pressed)
                key_pressed = break_key_pressed
                keyPressed = True
                current_key_pressed.add(break_key_pressed)

            elif total == 5:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "GAS", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                PressKey(accelerator_key_pressed)
                key_pressed = accelerator_key_pressed
                keyPressed = True
                current_key_pressed.add(accelerator_key_pressed)

        # If no gesture detected, release all keys
        if not keyPressed and len(current_key_pressed) != 0:
            for k in current_key_pressed:
                ReleaseKey(k)
            current_key_pressed.clear()

        # If switching keys, release the old one
        elif keyPressed and len(current_key_pressed) > 1:
            to_release = [k for k in current_key_pressed if k != key_pressed]
            for k in to_release:
                ReleaseKey(k)
                current_key_pressed.discard(k)

        cv2.imshow("Frame", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
