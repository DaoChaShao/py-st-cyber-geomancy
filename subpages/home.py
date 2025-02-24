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
    caption("If you use the models of **cc.en.300.vec** and **cc.zh.300.vec** to test the similarity locally, \
    you should be patient, because you have to take approximately 5 minutes for every single round.")
    caption("However, if you use the models of **en_core_web_lg** and **zh_core_web_md** to test locally, \
            you can get the result in a few seconds.")

empty_message: empty = empty()

empty_message.info("You can test the similarity between words in the Geomancy page.")
