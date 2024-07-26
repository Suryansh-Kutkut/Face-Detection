Download the casscade file , install the open cv in command !


Additional Comments in the Code:


cv2.CascadeClassifier("haarcascade_frontalface_default.xml"): Loads the pre-trained Haar Cascade Classifier for frontal face detection.


cv2.VideoCapture(0): Opens the default webcam (device 0) for capturing video.


b.read(): Reads a frame from the webcam.


cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY): Converts the captured frame to grayscale for face detection.


a.detectMultiScale(e, 1.3, 6): Detects faces in the grayscale frame.


cv2.rectangle(d_image, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 5): Draws rectangles around the detected faces.


cv2.imshow('Real-time Face Detection', d_image): Displays the frame with rectangles.


cv2.waitKey(40) & 0xff: Waits for 40ms between frames and checks for key presses.


cv2.getWindowProperty('Real-time Face Detection', cv2.WND_PROP_VISIBLE): Checks if the display window is still open.


b.release(): Releases the webcam.


cv2.destroyAllWindows(): Closes all OpenCV windows.
