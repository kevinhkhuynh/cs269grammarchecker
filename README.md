This project is a reimplementation of "Sentence-Level Grammatical Error Identification as Sequence-to-Sequence Correction" using Torch (only for tokenization), PyTorch, and OpenNMT-py.

The most recent version and documentation for OpenNMT is available here: https://github.com/OpenNMT/OpenNMT-py

Dependencies:

* `Torch`
* `bit32`
* `PyTorch`
* `coreutils`

GPU training requires:

* `cunn`
* `cutorch`

Multi-GPU training additionally requires:

* `threads`

## Instructions

Set up repo and Open-NMT-py:

1) git clone --recursive https://github.com/rollbackcc/cs269grammarchecker.git

3) pip install -r OpenNMT-py/requirements.txt

How to initialize the data-set:

1) Download the data set (Training data, development data, and Test data (with edits): http://textmining.lt/aesw/aesw2016down.html

2) Extract the three files and copy them as data/train.xml, data/dev.xml, and data/test.xml

3) Tokenize the data:

```./xml_to_tok```

How to create the Word-All Model:

1) Preprocess the data, train the model, translate sentences, and evaluate.

```./create_word_model```

How to create the Word-Sample Model:

1) Preprocess the data, train the model, translate sentences, and evaluate.

```./create_word_sample_model```
