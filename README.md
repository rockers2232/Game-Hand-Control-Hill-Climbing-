# 🕹️ Hand-Controlled Hill Climbing Game

Control your hill-climbing browser game using **just your hand gestures**! This project uses **OpenCV**, **MediaPipe**, and **keyboard simulation** to offer a touch-free game control experience.

---

## 📂 Project Structure

Game Hand Control Hill Climbing/
├── pycache/ # Auto-generated Python bytecode
├── directkeys.py # Script to simulate key presses
└── main.py # Main hand-tracking and control logic

---

## 🎯 Features

- 🖐️ Hand gesture detection using MediaPipe
- 🎮 Simulated keypresses (`Left` and `Right` arrow keys)
- 🪟 Auto-focuses on browser game using window name
- 🏎️ Designed for hill climbing games in the browser

---

## 🔧 Requirements

Install required packages and tools:

```bash
pip install opencv-python mediapipe
sudo apt install xdotool
🚀 How to Run
Open your browser and load your favorite hill climbing game (e.g. Hill Climb Racing).

Edit the window title in main.py if needed:

python
Copy
Edit
xdotool search --name 'Hill Climb' ...
Run the project:

bash
Copy
Edit
cd "Game Hand Control Hill Climbing"
python3 main.py
🎮 Controls (Default)
Hand Gesture	Action
Tilt Right	Accelerate
Tilt Left	Brake

🛠️ Files Explained
main.py – Uses MediaPipe and OpenCV to detect hand gestures and send commands.

directkeys.py – Contains logic to simulate key presses via xdotool.

🧠 Notes
Works best on Linux systems due to reliance on xdotool.

Ensure your webcam is connected and accessible.

👨‍💻 Author
Ayush Saini
GitHub: @rockers2232

📄 License
Licensed under the MIT License.
