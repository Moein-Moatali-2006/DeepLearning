import argparse
import cv2
from ultralytics import YOLO
from deep_text_recognition_benchmark.dtrb import DTRB


parser = argparse.ArgumentParser()
parser.add_argument('--workers', type=int, default=0)
parser.add_argument('--batch_size', type=int, default=192)
parser.add_argument('--batch_max_length', type=int, default=25)
parser.add_argument('--imgH', type=int, default=32)
parser.add_argument('--imgW', type=int, default=100)
parser.add_argument('--rgb', action='store_true')
parser.add_argument('--character', type=str, default='0123456789abcdefghijklmnopqrstuvwxyz')
parser.add_argument('--sensitive', action='store_true')
parser.add_argument('--PAD', action='store_true')
parser.add_argument('--Transformation', type=str, default="TPS")
parser.add_argument('--FeatureExtraction', type=str, default="ResNet")
parser.add_argument('--SequenceModeling', type=str, default="BiLSTM")
parser.add_argument('--Prediction', type=str, default="Attn")
parser.add_argument('--num_fiducial', type=int, default=20)
parser.add_argument('--input_channel', type=int, default=1)
parser.add_argument('--output_channel', type=int, default=512)
parser.add_argument('--hidden_size', type=int, default=256)
parser.add_argument('--detector_weights', type=str, default="weights/yolov8-detector/yolov8-s-license-plate-detector.pt")
parser.add_argument('--recognizer_weights', type=str, default="weights/dtrb-recognizer/dtrb-None-VGG-BiLSTM-CTC-license-plate-recognizer.pth")
parser.add_argument('--input_image', type=str, default="io/input/image_test.jpg")
parser.add_argument('--threshold', type=float, default=0.6)
opt = parser.parse_args()


class LicensePlate:
    def __init__(self, opt):
        self.opt = opt
        self.plate_detector = YOLO(opt.detector_weights)
        self.plate_recognizer = DTRB(opt.recognizer_weights, opt)
        self.image = cv2.imread(opt.input_image)
        self.plates_text = []  
    def process(self):
        results = self.plate_detector.predict(self.image)
        for result in results:
            for i in range(len(result.boxes.xyxy)):
                if result.boxes.conf[i] > self.opt.threshold:
                    bbox_tensor = result.boxes.xyxy[i]
                    bbox_ndarray = bbox_tensor.cpu().detach().numpy().astype(int)
                    print(bbox_ndarray)
                    x1, y1, x2, y2 = bbox_ndarray
                    plate_image = self.image[y1:y2, x1:x2].copy()

                    cv2.imwrite(f"io/output/plate_image_result_{i}.jpg", plate_image)
                    cv2.rectangle(self.image, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=4)

                    plate_image = cv2.resize(plate_image, (100, 32))
                    plate_image = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)

                    predicted_text = self.plate_recognizer.predict(plate_image, self.opt)
                    self.plates_text.append(predicted_text)  

        cv2.imwrite("io/output/image_result.jpg", self.image)



if __name__ == "__main__":
    lp = LicensePlate(opt)
    lp.process()
