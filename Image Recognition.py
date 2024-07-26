import cv2 #cv2 is used for neewer version of python!

# Load the Haar Cascade Classifier for face detection
a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open the webcam (usually webcam is device 0)
b = cv2.VideoCapture(0)

while True:
    # Read the frame from the webcam
    c_rec, d_image = b.read()
    
    # Convert the frame to grayscale
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    f = a.detectMultiScale(e, 1.3, 6)

    # Draw rectangles around the detected faces
    for (x1, y1, w1, h1) in f:
        cv2.rectangle(d_image, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 5)

    # Display the frame with the rectangles
    cv2.imshow('Real-time Face Detection', d_image)
    
    # Wait for 40ms and check if the 'Esc' key is pressed or the window is closed
    h = cv2.waitKey(40) & 0xff
    if h == 27:  # 'Esc' key has the ASCII code 27
        break
    if cv2.getWindowProperty('Real-time Face Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the webcam and destroy all OpenCV windows
b.release()
cv2.destroyAllWindows()
