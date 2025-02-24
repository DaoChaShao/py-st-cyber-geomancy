#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 19:14
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :   

from utilis.tools import is_model, similarity_checker, Timer


def main() -> None:
    """ streamlit run main.py """
    model_name: str = "cc.en.300"
    is_model(model_name)

    vocab_x: str = "cat"
    vocab_y: str = "dog"
    with Timer("Word Vector Similarity") as timer:
        similarity_checker(model_name, vocab_x, vocab_y)
    print(timer)


if __name__ == "__main__":
    main()
