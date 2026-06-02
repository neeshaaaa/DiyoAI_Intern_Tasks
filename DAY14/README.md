# Day 14 - Bigram Language Model from Scratch

## Objective

Today's goal was to understand the fundamentals of N-gram Language Models by implementing a **Bigram Language Model from scratch** using Python. The focus was on learning how statistical language models predict the next word based on the previous word.



## Topics Covered

* Introduction to N-gram Models
* Unigrams vs Bigrams
* Text Tokenization
* Special Tokens (`<START>`, `<END>`)
* Unigram Frequency Counts
* Bigram Frequency Counts
* Conditional Probability
* Next Word Prediction
* Sentence Generation
* Laplace (Add-1) Smoothing
* Sentence Probability Calculation

---

## What is a Bigram Model?

A Bigram Language Model estimates the probability of a word based on the word that comes immediately before it.

Formula:

P(word₂ | word₁) = Count(word₁, word₂) / Count(word₁)

Example:

Sentence:

I love machine learning

Generated Bigrams:

* (I, love)
* (love, machine)
* (machine, learning)

---

## Implementation Steps

### 1. Created a Small Text Corpus

A small dataset was defined inside the notebook for training the language model.

### 2. Tokenized the Text

Each sentence was split into individual words (tokens).

### 3. Added Special Tokens

Added:

* `<START>` to indicate the beginning of a sentence
* `<END>` to indicate the end of a sentence

### 4. Calculated Unigram Counts

Counted the frequency of each word in the corpus.

### 5. Calculated Bigram Counts

Counted how many times each pair of consecutive words appeared.

### 6. Computed Bigram Probabilities

Calculated conditional probabilities using bigram and unigram counts.

### 7. Implemented Next Word Prediction

Given a word, the model predicts the most likely next word.

Example:

Input:

I

Output:

love

### 8. Generated Sentences

Used learned bigram probabilities to generate simple sentences.

### 9. Applied Laplace Smoothing

Implemented Add-1 smoothing to handle unseen word pairs and avoid zero probabilities.

### 10. Calculated Sentence Probability

Computed the probability of an entire sentence using the chain of bigram probabilities.

---

## Key Learnings

* How statistical language models work
* Difference between unigrams and bigrams
* Importance of frequency counts in NLP
* How conditional probability is used for prediction
* Why smoothing is necessary
* Limitations of traditional N-gram models
* Foundation concepts behind modern language models

---

## Technologies Used

* Python
* Jupyter Notebook
* Collections Module
* Random Module
* Math Module

---

## Outcome

Successfully built a beginner-friendly Bigram Language Model from scratch and gained a practical understanding of N-gram based language modeling techniques used in Natural Language Processing (NLP).

---

## Future Improvements

* Implement Trigram Language Model
* Train on larger datasets
* Evaluate using Perplexity
* Compare with Neural Language Models
* Explore Transformer-based Language Models
