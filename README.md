# Semeval 2017 task 8 : RumourEval

*External participation in task 8 of Semeval 2017 : RumourEval: Determining rumour veracity and support for rumours*

## Description

Second approach of machine learning. Discovery of deep learning and dedicated libraries (Keras, Tensoflow).

### Purpose:

The purpose of this project is to classify comments to a tweet in several class - how, deny, support, query - relativly to the content of the tweets and its metadata.

The project has been divided into several steps:

- Create a parser of tweets comments and relevant metadata.
- Create a strong but simple statistical model for as a point of comparison (model Naive Bayes).
- Create a deep learning model with a simple hidden layer.
- Propose several vectorization of the inputs to obtain better results (Bag of word, n-grams, TF-IDF, metadata, ...).

### More informations:

read the [report](https://github.com/poggioenzo/semeval2017task8/blob/master/rapport.pdf).

---

## The code

All have been implemented in python3

### Libraries required:
- TensorFlow
- Keras
- sklearn
- json

### How to use this code & create useful datasets:

```
cd script
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

### Test a model hypX:

*Replace the X by [1, 2, 3, 4, 5, 6, 3bis, 6bis] to test a specific hypothesis*

- Naive bayes:
```
python3 nb.py hypX
```
- Neural network:
```
python3 nn.py hypX
```
