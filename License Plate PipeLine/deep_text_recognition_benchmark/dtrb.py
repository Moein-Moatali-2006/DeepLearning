import string
import argparse
import torch
import torch.backends.cudnn as cudnn
import torch.utils.data
import torch.nn.functional as F
import torchvision.transforms as transforms
import cv2

from deep_text_recognition_benchmark.utils import CTCLabelConverter, AttnLabelConverter
from deep_text_recognition_benchmark.dataset import RawDataset, AlignCollate
from deep_text_recognition_benchmark.model import Model


class DTRB:
    def __init__(self, weights_path, opt):
        if opt.sensitive:
            opt.character = string.printable[:-6]  

        cudnn.benchmark = True
        cudnn.deterministic = True
        opt.num_gpu = torch.cuda.device_count()

        """ model configuration """
        if 'CTC' in opt.Prediction:
            self.converter = CTCLabelConverter(opt.character)
        else:
            self.converter = AttnLabelConverter(opt.character)
        opt.num_class = len(self.converter.character)

        if opt.rgb:
            opt.input_channel = 3
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.load_model(weights_path, opt)

    def load_model(self, weights_path, opt):
        self.model = Model(opt)
        print('model input parameters', opt.imgH, opt.imgW, opt.num_fiducial, opt.input_channel, opt.output_channel,
            opt.hidden_size, opt.num_class, opt.batch_max_length, opt.Transformation, opt.FeatureExtraction,
            opt.SequenceModeling, opt.Prediction)
        self.model = torch.nn.DataParallel(self.model).to(self.device)

        
        print('loading pretrained model from %s' % weights_path)
        self.model.load_state_dict(torch.load(weights_path, map_location=self.device))

    def predict(self, image, opt):
        transform = transforms.Compose([
                transforms.ToTensor(),
            ])
            
        
        self.model.eval()
        with torch.no_grad():
            image_tensor = transform(image)
            image_tensor = image_tensor.sub_(0.5).div_(0.5)
            image_tensor = torch.unsqueeze(image_tensor, 0)  
            
            batch_size = image_tensor.size(0)
            image = image_tensor.to(self.device)

            length_for_pred = torch.IntTensor([opt.batch_max_length] * batch_size).to(self.device)
            text_for_pred = torch.LongTensor(batch_size, opt.batch_max_length + 1).fill_(0).to(self.device)

            if 'CTC' in opt.Prediction:
                preds = self.model(image, text_for_pred)

                
                preds_size = torch.IntTensor([preds.size(1)] * batch_size)
                _, preds_index = preds.max(2)
                preds_str = self.converter.decode(preds_index, preds_size)

            else:
                preds = self.model(image, text_for_pred, is_train=False)
                _, preds_index = preds.max(2)
                preds_str = self.converter.decode(preds_index, length_for_pred)

            dashed_line = '-' * 80
            head = f'{"image_path":25s}\t{"predicted_labels":25s}\tconfidence score'
            
            print(f'{dashed_line}\n{head}\n{dashed_line}')
            
            preds_prob = F.softmax(preds, dim=2)
            preds_max_prob, _ = preds_prob.max(dim=2)
            for img_name, pred, pred_max_prob in zip(["Test"], preds_str, preds_max_prob):
                if 'Attn' in opt.Prediction:
                    pred_EOS = pred.find('[s]')
                    pred = pred[:pred_EOS] 
                    pred_max_prob = pred_max_prob[:pred_EOS]

                
                confidence_score = pred_max_prob.cumprod(dim=0)[-1]

                print(f'{img_name:25s}\t{pred:25s}\t{confidence_score:0.4f}')
                return pred


if __name__ == "__main__":
    plate_recognizer = DTRB("../weights/dtrb-recognizer/dtrb-None-VGG-BiLSTM-CTC-license-plate-recognizer.pth")

    image = cv2.imread("../io/input/IMG_5157.JPG")
    plate_recognizer.predict(image)
