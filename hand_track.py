import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

prev_action = "none"

def fingers_up(hand_landmarks):
    tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky tips
    fingers = []

    for tip in tips:
        # Compare tip with its lower joint (knuckle)
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)  # Finger is up
        else:
            fingers.append(0)  # Finger is down

    return fingers

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    action = "none"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_states = fingers_up(hand_landmarks)
            total_fingers = sum(finger_states)

            if total_fingers == 0:
                action = "left"  # Fist
            elif total_fingers >= 4:
                action = "right"  # Open hand
            else:
                action = "none"  # In-between gestures = ignore

    if action != prev_action:
        pyautogui.keyUp("left")
        pyautogui.keyUp("right")

        if action == "left":
            pyautogui.keyDown("left")
        elif action == "right":
            pyautogui.keyDown("right")

        prev_action = action

    cv2.imshow("Gesture", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

pyautogui.keyUp("left")
pyautogui.keyUp("right")
cap.release()
cv2.destroyAllWindows()
