\# NLP Learning



A hands-on journey through core NLP concepts — built while working through CampusX's NLP playlist, applying each concept to real datasets rather than just following along.



\## Featured: Question Similarity Detection



A duplicate-question classifier, built progressively to understand how much feature representation matters before reaching for deep learning.



\*\*Approach:\*\*

| Stage | Notebook | Description |

|---|---|---|

| 1 | `00\_eda.ipynb` | Exploratory data analysis on the question pairs dataset |

| 2 | `01\_bow\_baseline.ipynb` | Baseline Bag-of-Words model |

| 3 | `02\_bow\_with\_preprocessing.ipynb` | Added text preprocessing + advanced feature engineering |



\*\*Result:\*\* 79.45% accuracy after preprocessing and feature engineering.



\*\*What I'd try next:\*\* word2vec or sentence embeddings to capture semantic similarity beyond word overlap, since BoW-based features struggle with paraphrased questions that share little surface vocabulary.



\## Other Notebooks



\- `text-preprocessing.ipynb` — Tokenization, stopword removal, lemmatization/stemming fundamentals

\- `text-classification.ipynb` — Text classification pipeline

\- `word2vec.ipynb` / `word2vec\_demo.ipynb` — Word embeddings from scratch and applied

\- `pos-tagging.ipynb` — Part-of-speech tagging using spaCy

\- `scrape.py` — Data collection script



\## Why this repo



I wanted to understand NLP from first principles — starting with sparse representations like BoW before moving to embeddings and transformer-based approaches (see my separate \[English-to-Nepali Transformer project](https://github.com/Anish494/English\_to\_nepali\_translator\_using\_transformer), built from scratch in PyTorch). This repo is where I test ideas and build intuition before applying them elsewhere.

