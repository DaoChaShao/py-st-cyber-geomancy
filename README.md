**INTRODUCTIONS**  
This application is designed to help you understand the word vectors and their features.

**RESOURCES**  
This application is using the pre-trained word vectors from the website of [FastText](https://fasttext.cc/), which
is specifically
located at the page of [Word vectors for 157 languages](https://fasttext.cc/docs/en/crawl-vectors.html).

The pre-trained word vectors in English and Chinese are used in this application. You can choose the language you want
to use.

**EXPLANATIONS**
If you use the models of `cc.en.300.vec` and `cc.zh.300.vec` to test the similarity locally, you should be patient,
because you have to take approximately 5 minutes for every single round. However, if you use the series models of *
*zh_core_web**, you need to run the following commands:
`python -m spacy download en_core_web_sm`, `python -m spacy download zh_core_web_sm`,
`python -m spacy download en_core_web_md`, `python -m spacy download zh_core_web_md`,
`python -m spacy download en_core_web_lg` and `python -m spacy download zh_core_web_lg`. When you test the similarity
using them locally, you can get the
result in a few seconds.

**LICENSE**  
[BSD 3-Clause License](LICENSE)
