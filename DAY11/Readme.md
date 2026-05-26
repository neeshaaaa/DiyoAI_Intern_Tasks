## Overview

This project is a beginner-friendly introduction to **Natural Language Processing (NLP)** using two popular Python libraries:

- NLTK
- spaCy

The notebook covers:

- Basic linguistics concepts
- Tokenization
- Stopword removal
- Stemming
- Lemmatization
- Part-of-Speech (POS) Tagging
- Named Entity Recognition (NER)
- Comparison between NLTK and spaCy

The goal of this project is to understand how machines process and analyze human language.

---

# What is NLP?

Natural Language Processing (NLP) is a field of Artificial Intelligence that enables computers to understand, process, and generate human language.

Applications of NLP include:

- Chatbots
- Machine Translation
- Speech Recognition
- Sentiment Analysis
- Search Engines
- Text Summarization
- Recommendation Systems

---

# Linguistics Concepts Covered

## 1. Morphology

Morphology is the study of word structure.

Example:

```text
unhappiness = un + happy + ness
```

---

## 2. Syntax

Syntax is the study of sentence structure and grammar.

Example:

```text
"The cat sits on the mat."
```

---

## 3. Semantics

Semantics is the study of meaning in language.

Example:

```text
"Apple" can refer to a fruit or a company depending on context.
```

---

## 4. Pragmatics

Pragmatics focuses on understanding meaning using context.

Example:

```text
"Can you open the door?"
```

This is interpreted as a request, not just a question.

---

# Topics Implemented

## Tokenization

Tokenization is the process of splitting text into smaller units called tokens.

Example:

```python
["I", "love", "NLP", "."]
```

Types of tokenization:

- Word Tokenization
- Sentence Tokenization

---

## Stopword Removal

Stopwords are common words that may not add much meaning to text analysis.

Examples:

```text
the, is, are, and, in
```

---

## Stemming

Stemming reduces words to their root forms mechanically.

Example:

```python
running -> run
studies -> studi
```

---

## Lemmatization

Lemmatization reduces words to their dictionary base form.

Example:

```python
running -> run
better -> good
```

---

## POS Tagging

Part-of-Speech Tagging assigns grammatical labels to words.

Example:

```python
("dog", "NN")
```

Where:

- NN = Noun
- VB = Verb
- JJ = Adjective

---

## Named Entity Recognition (NER)

NER identifies names of:

- People
- Organizations
- Countries
- Cities
- Dates

Example:

```text
Elon Musk -> PERSON
Google -> ORGANIZATION
Nepal -> GPE
```

---

# Technologies Used

- Python
- Jupyter Notebook
- NLTK
- spaCy

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
```

---

## Install Required Libraries

```bash
pip install nltk
pip install spacy
```

---

## Download spaCy English Model

```bash
python -m spacy download en_core_web_sm
```

---

## Download NLTK Resources

```python
import nltk

resources = [
    'punkt',
    'stopwords',
    'wordnet',
    'omw-1.4',
    'averaged_perceptron_tagger',
    'averaged_perceptron_tagger_eng',
    'maxent_ne_chunker',
    'maxent_ne_chunker_tab',
    'words'
]

for resource in resources:
    nltk.download(resource)
```

---

# Project Structure

DAY11/
│
├── Basic_linguistic.ipynb
├── README.md

---

# NLTK vs spaCy

| NLTK | spaCy |
|------|--------|
| Educational | Production-oriented |
| Good for learning | Faster processing |
| More manual | Cleaner API |
| Research focused | Industry focused |

---

# Example Output

## Tokenization

Input:

```text
"I love NLP."
```

Output:

```python
['I', 'love', 'NLP', '.']
```

---

## POS Tagging

Output:

```python
[
 ('The', 'DT'),
 ('cat', 'NN'),
 ('runs', 'VBZ')
]
```

---

## Named Entity Recognition

Output:

```text
Google -> ORGANIZATION
Kathmandu -> GPE
```

---

# Learning Outcomes

After completing this project, I learned:

- Basic linguistics concepts
- How tokenization works
- Text preprocessing techniques
- Difference between stemming and lemmatization
- POS tagging
- Named Entity Recognition
- Practical use of NLTK and spaCy

---
