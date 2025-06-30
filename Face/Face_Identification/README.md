# Face identification:

## face_bank:
in this directory there are some classes.
if you want to add a new class or remove a class you should add or delete the folder in face_dataset.

## create_face_bank.ipynb.
Models:
* antelopev2
* buffalo_l
* buffalo_m
* buffalo_s
* buffalo_sc

[models information](https://github.com/deepinsight/insightface/tree/master/python-package)

```python 
app = FaceAnalysis(name="buffalo_l", providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))
```

## face_identification.ipynb
input:

!["input"]()

output:

!["output"]()