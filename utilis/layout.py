#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 19:15
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :   

from streamlit import Page, navigation


def pages_layout():
    elements: dict = {
        "page": ["subpages/home.py", "subpages/geomancy.py"],
        "title": ["Home", "Geomancy"],
        "icon": [":material/home:", ":material/diversity_2:"],
    }

    structure: dict = {
        "Introduction": [
            Page(page=elements["page"][0], title=elements["title"][0], icon=elements["icon"][0]),
        ],
        "Models": [
            Page(page=elements["page"][1], title=elements["title"][1], icon=elements["icon"][1]),
        ],
    }
    pg = navigation(structure, position="sidebar", expanded=True)
    pg.run()
