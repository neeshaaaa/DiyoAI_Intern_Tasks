# NLP Text Preprocessing — Stopwords, Regex, Stemming & Lemmatization

## Overview

This project focuses on important **Natural Language Processing (NLP)** preprocessing techniques using Python and NLTK.

The notebook demonstrates how raw text is cleaned and transformed before applying machine learning or deep learning models.

Topics covered in this project:

- Stopwords
- Regular Expressions (Regex)
- Stemming
- Lemmatization
- Text Cleaning
- Basic NLP Preprocessing Pipeline

---

# What is NLP Preprocessing?

NLP preprocessing is the process of cleaning and preparing raw text data for analysis.

Raw text often contains:

- punctuation
- numbers
- special characters
- URLs
- emails
- unnecessary words

Preprocessing improves:

- text quality
- model performance
- processing speed
- consistency in NLP tasks

---

# Topics Covered

---

# 1. Stopwords

## Definition

Stopwords are very common words that usually do not carry significant meaning in many NLP tasks.

Examples:

```text
the, is, are, in, on, and, a, an
```

---

## Why Remove Stopwords?

Removing stopwords helps:

- reduce noise in text
- improve efficiency
- reduce dataset size
- focus on meaningful words

---

## Example

Original Sentence:

```text
"The cat is sitting on the mat."
```

After Stopword Removal:

```text
"cat sitting mat"
```

---

## Applications

- Search Engines
- Text Classification
- Sentiment Analysis
- Spam Detection
- Information Retrieval

---

# 2. Regular Expressions (Regex)

## Definition

Regular Expressions (Regex) are patterns used to search, match, and manipulate text.

Regex is widely used in NLP preprocessing and text cleaning.

---

## Common Uses of Regex

- Removing punctuation
- Removing numbers
- Extracting emails
- Extracting hashtags
- Extracting URLs
- Removing extra spaces

---

## Example

Original Text:

```text
"Hello!!! NLP is amazing."
```

After Cleaning:

```text
"Hello NLP is amazing"
```

---

## Common Regex Symbols

| Symbol | Meaning |
|---|---|
| `\d` | digit |
| `\w` | word character |
| `\s` | whitespace |
| `+` | one or more |
| `*` | zero or more |

---

# 3. Stemming

## Definition

Stemming is the process of reducing words to their root form by removing prefixes or suffixes mechanically.

The resulting word is called a stem.

---

## Examples

| Original Word | Stem |
|---|---|
| running | run |
| studies | studi |
| playing | play |

Some stems may not be valid dictionary words.

---

## Popular Stemming Algorithms

- Porter Stemmer
- Lancaster Stemmer
- Snowball Stemmer

---

## Advantages

- Fast
- Simple
- Reduces vocabulary size

---

## Disadvantages

- Less accurate
- May produce invalid words
- Ignores context

---

# 4. Lemmatization

## Definition

Lemmatization reduces words to their dictionary base form, known as the lemma.

Unlike stemming, lemmatization uses:

- grammar
- vocabulary
- part-of-speech information

to generate meaningful root words.

---

## Examples

| Original Word | Lemma |
|---|---|
| running | run |
| studies | study |
| cars | car |
| better | good |

---

## Advantages

- More accurate
- Produces valid dictionary words
- Context-aware

---

## Disadvantages

- Slower than stemming
- More computationally expensive

---


# Technologies Used

- Python
- NLTK
- Regular Expressions (re module)
- Jupyter Notebook

---

# Installation

## Install Required Libraries

```bash
pip install nltk
```

---

## Download NLTK Resources

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

---

# Project Structure

DAY12/
│
├── text_Preprocessing_NLP.ipynb
├── README.md

---

# Example Workflow

The preprocessing pipeline includes:

1. Lowercasing text
2. Regex cleaning
3. Tokenization
4. Stopword removal
5. Stemming
6. Lemmatization

---

# Learning Outcomes

After completing this project, I learned:

- Importance of NLP preprocessing
- Stopword removal techniques
- Regex pattern matching
- Text cleaning methods
- Difference between stemming and lemmatization
- Basic NLP preprocessing pipeline creation

---



