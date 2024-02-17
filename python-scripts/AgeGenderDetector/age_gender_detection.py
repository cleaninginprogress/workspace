import cv2
import numpy as np

face_model = cv2.dnn.readNet('opencv_face_detector_uint8.pb', 'opencv_face_detector.pbtxt')
age_model = cv2.dnn.readNet('age_net.caffemodel', 'age_deploy.prototxt')
gender_model = cv2.dnn.readNet('gender_net.caffemodel', 'gender_deploy.prototxt')

MODEL_MEAN_VALUES = (78.4263377603,  87.7689143744,  114.895847746)

age_categories = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
gender_categories = ['Male', 'Female']

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame,  1.0, (300,  300), MODEL_MEAN_VALUES, swapRB=True, crop=False)
    face_model.setInput(blob)
    detections = face_model.forward()

    face_boxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0,  0, i,  2]
        if confidence >  0.7:
            x1, y1, x2, y2 = map(int, detections[0,  0, i,  3:7]*np.array([w, h, w, h]))
            face_boxes.append([x1, y1, x2, y2])

    for face_box in face_boxes:
        face = frame[face_box[1]:face_box[3], face_box[0]:face_box[2]]
        blob = cv2.dnn.blobFromImage(face,  1.0, (227,  227), MODEL_MEAN_VALUES, swapRB=False)
        gender_model.setInput(blob)
        gender_preds = gender_model.forward()
        gender = gender_categories[gender_preds[0].argmax()]

        age_model.setInput(blob)
        age_preds = age_model.forward()
        age = age_categories[age_preds[0].argmax()]

        cv2.putText(frame, f'{gender}, {age}', (face_box[0], face_box[1]-10), cv2.FONT_HERSHEY_SIMPLEX,  0.9, (36,255,12),  2)

    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) &  0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()