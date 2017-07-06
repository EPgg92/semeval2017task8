# SE8-2017

Libraries required:
- TensorFlow
- Keras
- sklearn
- json



How to use this code:

```
cd SE8-2017/script
```

Create useful datasets:

```
mkdir ../datasets/my_datasets
python3 create_new_datasets
python3 create_dic_directe_structure.py
python3 create_label.py
python3 create_vecs_hyp1.py
python3 create_vecs_hyp2.py
python3 create_vecs_hyp3.py
python3 create_vecs_hyp3bis.py
python3 create_vecs_hyp4.py
python3 create_vecs_hyp5.py
python3 create_vecs_hyp6.py
python3 create_vecs_hyp6bis.py
```

Test a model hypX:

(X = 1, 2, 3, 4, 5, 6, 3bis, 6bis)
- Naive bayes:
```
python3 nb.py hypX
```
- Neural network:
```
python3 nn.py hypX
```
