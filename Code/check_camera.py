def camer():
    import cv2

    # Load the cascade
    cascade_face = cv2.CascadeClassifier('haarcascade_default.xml')

    # To capture video from webcam.
    cap = cv2.VideoCapture(0)

    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = cascade_face.detectMultiScale(gray, 1.3, 5, minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)

        # Draw the rectangle around each face
        for (a, b, c, d) in faces:
            cv2.rectangle(img, (a, b), (a + c, b + d), (10,159,255), 2)


        # Display
        cv2.imshow('Webcam Check', img)

        # Stop if escape key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the captureVideo object
    cap.release()
    cv2.destroyAllWindows()
