#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/25 00:04
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   scapy.py
# @Desc     :   

from spacy import load
from streamlit import empty, sidebar, button, spinner

from utilis.tools import (params_scapy, model_checker,
                          similarity_scapy, plot_similarity_scapy)

empty_message: empty = empty()

model_name, word_x, word_y = params_scapy()

model_checker(model_name, empty_message)
# python -m spacy download en_core_web_lg
nlp = load(model_name)

with sidebar:
    check = button("Check Similarity", type="primary", help="Check the similarity between two words.")

if check:
    with spinner("The relationship between names is Calculating...", show_time=True):
        similarity: float = similarity_scapy(nlp, word_x, word_y, empty_message)
        plot_similarity_scapy(similarity, word_x, word_y)
