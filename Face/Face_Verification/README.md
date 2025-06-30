# 🧠 Face Verification

A simple Python project to compare two face images and determine whether they belong to the **same person** or **different individuals**, using [InsightFace](https://github.com/deepinsight/insightface).

---

## ⚙️ Installation

Install required libraries:

```bash
pip install -r requirements.txt

```
## 📸 Usage

1. Load Your Images:
```python
image_1 = cv2.imread("path/to/image1.jpg")
image_2 = cv2.imread("path/to/image2.jpg")
```

2. Set the Threshold:
```python
threshold = 22  # Lower = stricter, Higher = more lenient
```

3. Run Verification:

```text
✅ Same Person
❌ Different Persons
```

## 🧪 How It Works:
* Extract face embeddings from both images
* Compute the Euclidean distance between the two embeddings
* Compare the distance to the threshold