# Virtual-Mouse
This project allows you to control your computer's mouse cursor using hand gestures in real-time. Using MediaPipe for hand tracking, OpenCV for video capture, and PyAutoGUI for mouse control, this system simulates various mouse actions based on your hand movements.

<b>Project Overview:</b>

The Virtual Mouse project allows users to interact with their computer by moving the mouse cursor, clicking, and scrolling using only their hands. The project tracks the movement of your hand through a webcam feed and translates that into mouse input.

<b>Features:</b>
<ul>
<li>Cursor Movement: Control the mouse cursor by simply moving your hand.</li>
<li>Left Click: Simulate a left-click by bringing the index finger and thumb close together (less than 50 pixels apart).</li>
<li>Right Click: Perform a right-click by positioning the index finger and pinky finger close together (within 8 pixels vertically).</li>
<li>Scroll Up: Simulate scrolling up by bringing the index finger and pinky finger within 20 pixels vertically.</li>
<li>Scroll Down: Simulate scrolling down by bringing the index finger and index finger's MCP joint within 10 pixels vertically.</li>
</ul>  
The system uses your webcam to track hand movements, and based on proximity and specific gestures between fingers, it performs the associated actions.

<b>How It Works:</b>

1. Webcam Feed
The webcam continuously captures video, and the system processes each frame in real-time to detect hand positions.

2. Hand Detection
The system uses MediaPipe’s Hand model to detect and track key points on the hand (such as the index finger, thumb, and pinky). The proximity of these key points is used to interpret gestures.

3. Mouse Actions
Cursor Movement: When the index finger is detected by the webcam, the cursor moves along with the index finger.
Left Click: When the index finger and thumb are less than 50 pixels apart vertically, the system simulates a left-click.
Right Click: When the index finger and pinky finger are within 8 pixels vertically, the system performs a right-click.
Scroll Down: If the index finger and its MCP joint are within 10 pixels vertically, the system simulates a scroll down action.
Scroll Up: When the index finger and pinky finger are within 20 pixels vertically, the system simulates a scroll up action.

4. Real-Time Processing
The system processes the webcam feed at a stable frame rate to ensure smooth and responsive control. As you move your hand or perform gestures, the cursor follows in real-time, with specific gestures triggering the respective mouse actions. 
