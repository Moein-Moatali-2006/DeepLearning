from ultralytics import YOLO

plate_detector = YOLO("weights\yolov8-detector\yolov8-s-license-plate-detector.pt")

plate_detector.predict("io\input/1.png",save=True,save_crop=True)