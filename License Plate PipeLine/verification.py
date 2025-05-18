import sqlite3
import argparse
from identification import LicensePlate


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

plate = LicensePlate(opt)
plate.process()

conn = sqlite3.connect("Database_verification.db")
cursor = conn.cursor()

for text in plate.plates_text:
    cursor.execute("SELECT * FROM LicensePlate WHERE Plate = ?;", (text,))
    result = cursor.fetchone()

    if result:
        print(f"License plate {text} has been detected ✅")
    else:
        print(f"License plate {text} was not found in the database ❌")

conn.close()
