#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 19:16
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :   

from streamlit import title, divider, expander, caption, empty

title("Cyber Geomancy via Names")
divider()
with expander("Introduction", expanded=True):
    caption("Cyber Geomancy is a project that uses the Word2Vec model to analyze the similarity between words.")
    caption("The project is based on the Gensim library and the Streamlit framework.")
    caption("The project is a demonstration of the use of pre-trained models in the field of NL Processing.")

empty_message: empty = empty()

empty_message.info("You can test the similarity between words in the Geomancy page.")
