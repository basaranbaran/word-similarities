# Word Similarities

## Overview

The `word-similarities` component is a Python script that uses the Word2Vec model to calculate word similarities and perform word analogy tasks.

## Description

This script allows users to input two words and calculates their similarity using a pre-trained Word2Vec model. It also provides the most similar words to the given words and performs word analogy tasks.

## Usage

1. Ensure you have the required libraries installed: (You can also install the requirements.txt file)
    ```bash
    pip install gensim
    ```

2. Run the script:
    ```bash
    python word-similarities.py
    ```

3. Follow the prompts to input words and view the results.

## Example

```plaintext
if you want to exit, please write 'exit'
word1 input= First word: king
word2 input = Second word: queen
king and queen similarity: 0.65109557
king and car similarity: 0.10580277
queen and car similarity: 0.07896534
king and apple similarity: 0.14443234

Similar words to king:
monarch: 0.71181923
prince: 0.53773212
duke: 0.52021635
kings: 0.50887656
queen: 0.45157397

Similar words to queen:
princess: 0.71181923
monarch: 0.53773212
duchess: 0.52021635
kings: 0.50887656
king: 0.45157397

word3 input = word to be extracted from word1: man
king - man + woman = ?
queen: 0.71181923