#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 19:14
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tools.py
# @Desc     :   

from enum import unique, StrEnum
from gensim.models import KeyedVectors
from os import path
from pandas import DataFrame
from streamlit import (sidebar, header, selectbox, caption, text_input,
                       empty, markdown, bar_chart, data_editor)
from time import perf_counter


def is_model(model_name: str):
    """ Analysis of whether the pre-trained model exists """
    model_path = f"models/{model_name}.vec"

    if path.exists(model_path):
        print("The model exists!")
        return True
    else:
        print("The model does not exist!")
        return False


def model_size_getter(model_name: str) -> str:
    """ Get the size of the pre-trained model """
    model_path = f"models/{model_name}.vec"
    size: int = path.getsize(model_path)
    if size < 1024:
        out: str = f"{size} Bytes"
    elif size < 1024 ** 2:
        out: str = f"{size / 1024:.2f} KB"
    elif size < 1024 ** 3:
        out: str = f"{size / 1024 ** 2:.2f} MB"
    else:
        out: str = f"{size / 1024 ** 3:.2f} GB"
    return out


def is_lang(model_name: str, vocab_x: str, vocab_y: str) -> bool:
    """ Check the language of the pre-trained model """
    if "en" in model_name and vocab_x.isascii() and vocab_y.isascii():
        return True
    elif "zh" in model_name and not vocab_x.isascii() and not vocab_y.isascii():
        return True
    else:
        return False


def similarity_checker(model_name: str, vocab_x: str, vocab_y: str, messages: empty,
                       precision: int = 2) -> float | None:
    """ Check the similarity between two words """
    model_path = f"models/{model_name}.vec"

    model = KeyedVectors.load_word2vec_format(model_path, binary=False)

    word_x, word_y = vocab_x, vocab_y

    if is_lang(model_name, word_x, word_y):
        if word_x in model.key_to_index and word_y in model.key_to_index:
            similarity = model.similarity(word_x, word_y)
            print(f"The Cosine Similarity between {word_x} and {word_y} is: {similarity:.{precision}f}")
            return similarity
        elif word_x not in model.key_to_index:
            print(f"{word_x} is not in the vocabulary.")
            markdown(f"**{word_x}** is not in the vocabulary.")
        else:
            print(f"**{word_y}** is not in the vocabulary.")
            markdown(f"**{word_y}** is not in the vocabulary.")
    else:
        print("The language of the model and the words are not matched.")
        messages.error("The language of the model and the words are not matched.")


class Timer(object):

    def __init__(self, message: empty, description: str, precision: int = 5):
        self._message = message
        self._description = description
        self._precision = precision
        self._start = None
        self._end = None
        self._elapsed = None

    def __enter__(self):
        self._start = perf_counter()
        print(f"{self._description} is calculating...")
        self._message.warning(f"{self._description} is calculating...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = perf_counter()
        self._elapsed = self._end - self._start
        return False

    def __repr__(self):
        if self._elapsed is not None:
            self._message.success(
                f"{self._description} is completed, which takes {self._elapsed:.{self._precision}f} seconds.")
            return f"{self._description} takes {self._elapsed:.{self._precision}f} seconds."
        else:
            self._message.error(f"{self._description} is failed to cal.")
            return f"{self._description} is failed to cal."


def params() -> tuple[str, str, str]:
    with sidebar:
        header("Parameters")
        options: list = ["cc.en.300", "cc.zh.300"]
        model_name: str = selectbox("Model Name", options, index=0, help="Select the pre-trained model.")
        if is_model(model_name):
            caption(f"The size of the model {model_name} is: {model_size_getter(model_name)}.")
        else:
            caption("The model does **NOT** exist!")

        vocab_x: str = text_input("Enter One Name", value="Tom",
                                  placeholder="Enter One Name",
                                  help="Input the first word.")
        caption(f"The first word you entered is: **{vocab_x}**.")
        vocab_y: str = text_input("Enter Another Name", value="Jerry",
                                  placeholder="Enter Another Name",
                                  help="Input the second word.")
        caption(f"The second word you entered is: **{vocab_y}**.")

        return model_name, vocab_x, vocab_y


@unique
class Colour(StrEnum):
    RED: str = "#FFAAAA"
    YELLOW: str = "#FFEEAA"
    BLUE: str = "#88EEFE"
    GREEN: str = "#AAFFAA"
    GRAY: str = "#525352"


def plot_similarity(value: float, vocab_x: str, vocab_y: str) -> None:
    # Prepare the data for the bar chart
    data = DataFrame({"similarity": [value]})
    data_editor(data, disabled=True, hide_index=True, use_container_width=True)

    if 0 < value < 1:
        result: str = "Completely Identical"
        colour = Colour.GREEN
        geo: str = "You are CLOSE to each other!"
    elif value == 0:
        result: str = "No Similarity"
        colour = Colour.GRAY
        geo: str = "You are NEUTRAL!"
    else:
        result: str = "Completely Opposite"
        colour: str = Colour.RED
        geo: str = "You are FAR AWAY from each other!"

    title: str = f"The Similarity Result between {vocab_x} and {vocab_y} is {result}"
    markdown(f"##### {title}")
    bar_chart(data, x=None, color=colour, use_container_width=True)
    markdown(f"##### {geo}")
