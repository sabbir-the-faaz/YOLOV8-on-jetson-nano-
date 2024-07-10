#working but labels are not showing 
from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO("best.pt")

# Run predictions on the default webcam (source=0)
model.predict(
    source=0,             # Use the default webcam
    show=True,            # Display the video with predictions
    save=False,           # Do not save the prediction results
    hide_labels=False,    # Show labels on detected objects
    hide_conf=False,      # Show confidence scores
    conf=0.5,             # Confidence threshold of 0.5
    save_txt=False,       # Do not save results to a text file
    save_crop=False,      # Do not save cropped images of detected objects
    line_thickness=2,     # Set bounding box line thickness
    box=True,             # Draw bounding boxes
    visualize=False       # Do not use additional visualization options
)


