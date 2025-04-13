# HandGestureGameController
Control PC games using real-time hand gestures with Python + MediaPipe

# 🕹️ Hand Gesture Game Controller 🎮

This project lets you **play games like Hill Climb Racing using hand gestures** detected through your webcam. No keyboard needed – just ✋ and ✊ to control the game!

## 🔥 Features

- Real-time hand detection using **MediaPipe**
- Recognizes:
  - ✊ (Fist) → Move Left
  - ✋ (Open Hand) → Move Right
- Works with any PC game using keyboard arrows
- Fun and interactive way to experience gesture control

## 🧠 How it works

The system uses:
- **OpenCV** for webcam feed
- **MediaPipe** to detect hand landmarks
- **PyAutoGUI** to simulate keyboard key presses
- Custom logic to differentiate between open and closed hand based on finger landmarks

## 📂 Project Structure

