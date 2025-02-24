#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 19:14
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tools.py
# @Desc     :   

from gensim.models import KeyedVectors
from os import path
from streamlit import markdown
from time import perf_counter


def is_model(model_name: str):
    """ Analysis of whether the pre-trained model exists """
    model_path = f"models/{model_name}.vec"

    if path.exists(model_path):
        print("The model exists!")
    else:
        print("The model does not exist!")


def similarity_checker(model_name: str, vocab_x: str, vocab_y: str):
    """ Check the similarity between two words """
    model_path = f"models/{model_name}.vec"

    model = KeyedVectors.load_word2vec_format(model_path, binary=False)

    word_x, word_y = vocab_x, vocab_y

    if word_x in model.key_to_index and word_y in model.key_to_index:
        similarity = model.similarity(word_x, word_y)
        print(f"The similarity between {word_x} and {word_y} is: {similarity:.5f}")
    elif word_x not in model.key_to_index:
        print(f"'{word_x}' is not in the vocabulary.")
    else:
        print(f"'{word_y}' is not in the vocabulary.")


class Timer(object):

    def __init__(self, description: str, precision: int = 5):
        self._description = description
        self._precision = precision
        self._start = None
        self._end = None
        self._elapsed = None

    def __enter__(self):
        self._start = perf_counter()
        print(f"{self._description} is calculating...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = perf_counter()
        self._elapsed = self._end - self._start
        return False

    def __repr__(self):
        if self._elapsed is not None:
            return f"{self._description} takes {self._elapsed:.{self._precision}f} seconds."
        else:
            return f"{self._description} is failed to cal."
