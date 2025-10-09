import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
animal_classes = [15, 16, 17, 18, 19, 20, 21, 22]
def detect_animals(image_path):
    img = cv2.imread(image_path)
    results = model(img, classes=animal_classes)
    boxes = results[0].boxes
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    count = len(boxes)
    cv2.putText(img, f"Detected Animals: {count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Animal Detection Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_path = input("Enter image file path: ")
detect_animals(image_path)