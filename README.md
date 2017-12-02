This project is a reimplementation of "Sentence-Level Grammatical Error Identification as Sequence-to-Sequence Correction" using Torch (only for tokenization), PyTorch, and OpenNMT-py.

# OpenNMT: Open-Source Neural Machine Translation

The most recent version and documentation for OpenNMT is available here: https://github.com/opennmt/opennmt

* `Torch`
* `PyTorch`
* `bit32`

GPU training requires:

* `cunn`
* `cutorch`

Multi-GPU training additionally requires:

* `threads`

## Quickstart

How to create the word model

1) Download the data set (Training data, development data, and Test data (with edits): http://textmining.lt/aesw/aesw2016down.html

2) Extract the three files and copy them as data/train.xml, data/dev.xml, and data/testwithedits.xml

3) Tokenize the data:

```./xml_to_tok```

4) Preprocess the data, train the model, translate sentences, and evaluate.

```./create_word_model```

## OpenNMT Citation

A <a href="https://arxiv.org/abs/1701.02810">technical report</a> on OpenNMT is available. If you use the system for academic work, please cite:

```
    @ARTICLE{2017opennmt,
         author = { {Klein}, G. and {Kim}, Y. and {Deng}, Y.
                    and {Senellart}, J. and {Rush}, A.~M.},
         title = "{OpenNMT: Open-Source Toolkit
                   for Neural Machine Translation}",
         journal = {ArXiv e-prints},
         eprint = {1701.02810} }
```
