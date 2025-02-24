#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 19:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   geomancy.py
# @Desc     :

from random import uniform
from streamlit import empty, sidebar, button, spinner

from utilis.tools import (params, is_model, similarity_checker,
                          Timer, plot_similarity)

empty_messages: empty = empty()

model_name, vocab_x, vocab_y = params()

if is_model(model_name):
    empty_messages.info(f"The model **{model_name.upper()}** exists.")
else:
    empty_messages.error(f"The model **{model_name.upper()}** does not exist.")

with sidebar:
    check = button("Check Similarity", type="primary", help="Check the similarity between two words.")

if check:
    with Timer(empty_messages, "Word Vector Similarity") as timer:
        with spinner("The relationship between names is Calculating...", show_time=True):
            similarity: float = similarity_checker(model_name, vocab_x, vocab_y, empty_messages)
            # similarity: float = uniform(-1.0, 1.0)
            plot_similarity(similarity, vocab_x, vocab_y)

    empty_messages.success(timer)
