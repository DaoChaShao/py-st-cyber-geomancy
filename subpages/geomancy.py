#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 19:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   geomancy.py
# @Desc     :

from streamlit import empty, sidebar, button

from utilis.tools import params, is_model, similarity_checker, Timer

empty_messages: empty = empty()

model_name, vocab_x, vocab_y = params()

if is_model(model_name):
    empty_messages.info(f"The model **{model_name.upper()}** exists.")
else:
    empty_messages.error(f"The model **{model_name.upper()}** does not exist.")

with sidebar:
    check = button("Check Similarity", type="primary", help="Check the similarity between two words.")

if check:
    empty_messages.warning("Please wait for the result...")

    with Timer("Word Vector Similarity") as timer:
        similarity_checker(model_name, vocab_x, vocab_y)

    empty_messages.success(timer)
