# 🧠 Face Identification

This project demonstrates **face recognition and identification** using [InsightFace](https://github.com/deepinsight/insightface) and custom face banks.

---

## 📁 Directory: `face_bank/`

Each subfolder in this directory represents a **class/person**.  
To **add** or **remove** identities:

- ➕ Add a folder (with face images) to `face_dataset/`
- ➖ Remove the corresponding folder to delete a class

---

## ⚙️ Create Face Bank

Use the Jupyter notebook `create_face_bank.ipynb` to generate a face bank from the dataset.

### Supported Models:

- `antelopev2`
- `buffalo_l`
- `buffalo_m`
- `buffalo_s`
- `buffalo_sc`

👉 [Model details](https://github.com/deepinsight/insightface/tree/master/python-package)

### Example:

```python
from insightface.app import FaceAnalysis

app = FaceAnalysis(name="buffalo_l", providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

```

## 🧪 Face Identification Demo
🔻 Input Image:

!["input"](https://github.com/Moein-Moatali-2006/DeepLearning/blob/main/Face/Face_Identification/input.jpg)

🔺 Output (Labeled Faces):

!["output"](https://github.com/Moein-Moatali-2006/DeepLearning/blob/main/Face/Face_Identification/output.jpg)

Powered by InsightFace & OpenCV.