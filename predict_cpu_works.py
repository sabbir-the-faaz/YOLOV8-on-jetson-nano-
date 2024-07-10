import cv2
import torch
from ultralytics import YOLO

# Load the model
model = YOLO('best.pt')

# Ensure model runs on CPU
model.to('cpu')

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run inference
    results = model.predict(source=frame, show=True, conf=0.5, device='cpu')
    
    # Print results
    for result in results:
        print(result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
