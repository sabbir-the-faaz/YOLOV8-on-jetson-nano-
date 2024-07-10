import cv2
from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO("best.pt")

# Define a function to draw labels
def draw_labels(frame, predictions):
    for pred in predictions:
        # Get bounding box coordinates
        x1, y1, x2, y2 = map(int, pred['box'])
        label = pred['label']
        confidence = pred['confidence']

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Draw label with confidence
        label_text = f"{label}: {confidence:.2f}"
        cv2.putText(frame, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Run predictions on the default webcam (source=0)
for result in model.predict(source=0, show=True, conf=0.5):
    frame = result.imgs[0]
    draw_labels(frame, result.predictions)
    cv2.imshow("YOLO", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
