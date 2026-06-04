# 📰 NLP Text Preprocessing & Analysis Pipeline
### Applied on Real CNBC News Headlines Dataset

---

##  Project Overview

This project builds a complete **Natural Language Processing (NLP) pipeline** from scratch using **NLTK** and **spaCy** — two of the most widely used NLP libraries in Python. The pipeline is applied on a real-world dataset of **553 CNBC news headlines** scraped from the CNBC website, covering categories like Business News, Markets, Technology, Politics, and Investing.

The goal is to preprocess raw text data and extract meaningful information through a series of NLP techniques, ending with a similarity analysis that finds the most related headline pairs.

---

##  Dataset

| Property | Details |
|----------|---------|
| **Source** | CNBC News (cnbc_news_data.csv) |
| **Total Headlines** | 553 |
| **Key Column Used** | `title` (news headline) |
| **Other Columns** | `category`, `author`, `published_at` |
| **Categories** | Business News, Markets, Technology, Politics, Investing, CNBC TV, and more |
| **Date Range** | 2007 – 2024 |

---

##  Libraries & Tools Used

| Library | Purpose |
|---------|---------|
| `nltk` | Tokenization, POS Tagging |
| `spacy` | Named Entity Recognition (NER) |
| `scikit-learn` | TF-IDF Vectorization, Cosine Similarity |
| `pandas` | Data loading and manipulation |

---

##  Pipeline Steps

### 1.  Setup & Installation

Install all required libraries and download NLTK data packages (`punkt`, `averaged_perceptron_tagger`). Load the spaCy English model `en_core_web_sm` for NER processing.

---

### 2.  Load & Explore the Dataset

Load the CNBC CSV file using `pandas`. Select only the relevant columns (`title`, `category`, `author`, `published_at`). Drop any rows with missing headlines. Explore the dataset by checking how many articles exist per category and reviewing sample headlines.

---

### 3.  Tokenization

**Definition:**
Tokenization is the process of splitting raw text into individual units called **tokens** (words, punctuation, numbers). It is the very first and most fundamental step in any NLP pipeline.

**What we did:**
Applied NLTK's `word_tokenize()` function to every headline in the dataset. Each headline is converted from a full sentence into a list of individual tokens.

**Example:**
```
Input  : "Foxconn to invest $600 million in India"
Output : ['Foxconn', 'to', 'invest', '$', '600', 'million', 'in', 'India']
```

**Why it matters:**
Computers cannot process whole sentences directly. Tokenization breaks text into manageable pieces so that every next step — tagging, entity recognition, vectorization — can work properly.

**Use Cases:**
- Search engines splitting queries into keywords
- Chatbots understanding individual words in a message
- Autocomplete suggestions in text editors

---

### 4.  POS Tagging (Part-of-Speech Tagging)

**Definition:**
POS Tagging assigns a **grammatical label** to each token — identifying whether it is a noun, verb, adjective, preposition, etc.

**Common POS Tags:**

| Tag | Meaning | Example |
|-----|---------|---------|
| NNP | Proper Noun | Foxconn, Harvard, India |
| NN | Common Noun | market, deal, rate |
| VBZ | Verb (present) | rises, falls, announces |
| JJ | Adjective | strong, new, major |
| IN | Preposition | in, of, on, for |

**What we did:**
Applied NLTK's `pos_tag()` function on the token lists. Counted and analyzed the most frequently occurring POS tags across all 553 CNBC headlines to understand what types of words dominate financial news.

**Example:**
```
Headline : "Apple shares fall after earnings report"
POS Tags : [('Apple','NNP'), ('shares','NNS'), ('fall','VBP'), ('after','IN'), ('earnings','NNS'), ('report','NN')]
```

**Why it matters:**
POS tags reveal the grammatical structure of a sentence. In news text, proper nouns (NNP) carry the most information — they point to companies, people, and countries central to the story.

**Use Cases:**
- Grammar checkers (Microsoft Word, Grammarly)
- Text summarization (extracting key nouns and verbs)
- Question answering systems

---

### 5.  Named Entity Recognition (NER)

**Definition:**
NER is an NLP technique that **finds and classifies named real-world entities** in text — such as organizations, people, locations, monetary values, and dates.

**Entity Types Detected:**

| Label | Meaning | CNBC Example |
|-------|---------|--------------|
| ORG | Organization | Foxconn, Harvard, Apple |
| GPE | Country/City | India, New Jersey, China |
| PERSON | Person name | Meredith Whitney, Chris Christie |
| MONEY | Monetary value | $600 million, $2.25 billion |
| DATE | Date or time expression | Tuesday, last year, 2023 |

**What we did:**
Used **spaCy's** `en_core_web_sm` model to run NER on every headline. Extracted all entity-label pairs and identified the top 15 most frequently mentioned entities across the dataset. Also used spaCy's built-in `displacy` visualizer to render color-coded entity highlights directly in the Jupyter notebook.

**Example:**
```
Headline : "iPhone maker Foxconn to invest $600 million into phone and chip project in India"
Entities : [('Foxconn', 'ORG'), ('$600 million', 'MONEY'), ('India', 'GPE')]
```

**Why it matters:**
NER extracts structured, actionable facts from unstructured news text. Instead of reading an entire article, NER immediately tells you *who* is involved, *where* it happened, and *how much* money is at stake.

**Use Cases:**
- Financial news monitoring (tracking company mentions)
- Automated news categorization and tagging
- Building knowledge graphs from news data
- Powering search and recommendation engines

---

### 6.  TF-IDF Vectorization

**Definition:**
TF-IDF stands for **Term Frequency – Inverse Document Frequency**. It is a numerical method that converts text documents into vectors of numbers, where each number represents the importance of a word.

**How the score works:**
- **TF (Term Frequency):** How often a word appears in one headline
- **IDF (Inverse Document Frequency):** How rare the word is across all 553 headlines
- **TF-IDF Score = TF × IDF** → High score = important and unique word; Low score = common and unimportant word

**What we did:**
Used `scikit-learn`'s `TfidfVectorizer` with `stop_words='english'` to automatically remove common words like "the", "a", "is", "in". Built a TF-IDF matrix of shape **(553 headlines × 500 unique words)**. Displayed the top scoring words for each headline to understand which terms are most distinctive.

**Example:**
```
Headline : "Foxconn to invest $600 million in India"
Top TF-IDF words : [('foxconn', 0.52), ('invest', 0.48), ('million', 0.41), ('india', 0.38)]
```

**Why it matters:**
Machine learning and NLP models need numbers, not text. TF-IDF is the most standard and reliable way to represent documents mathematically while giving more weight to meaningful, distinctive words.

**Use Cases:**
- Document classification (spam detection, news categorization)
- Information retrieval (search engines)
- Feature engineering for machine learning models
- Content recommendation systems

---

### 7.  Cosine Similarity

**Definition:**
Cosine Similarity measures **how similar two documents are** by calculating the angle between their TF-IDF vectors in multi-dimensional space.

**Score Interpretation:**

| Score | Meaning |
|-------|---------|
| 1.0 | Identical content / very similar topic |
| 0.5 – 0.9 | Strongly related headlines |
| 0.1 – 0.4 | Somewhat related |
| 0.0 | Completely different topics |

**What we did:**
Computed cosine similarity between **every possible pair** of the 553 headlines using `scikit-learn`'s `cosine_similarity()`. Collected all pairs with a score greater than 0, sorted them from highest to lowest, and displayed the **Top 10 most similar headline pairs** with their categories and scores. Also analyzed whether similar headlines tend to come from the same category.

**Example Output:**
```
#1  Score: 0.8741
  → [Markets] Oil markets' decades-long dependence on China could be ending
  → [Markets] Fear Miners Set to Fall Off 'Supercycle'
```

**Why it matters:**
Cosine similarity is the backbone of how news platforms like Google News, Reuters, and Bloomberg cluster and relate thousands of articles automatically — without any human labeling.

**Use Cases:**
- Duplicate article detection in news aggregators
- "Related Articles" recommendation on websites
- Document clustering and topic grouping
- Plagiarism detection systems

---

##  Key Results

| Metric | Value |
|--------|-------|
| Total headlines analyzed | 553 |
| News categories covered | 15+ |
| Average tokens per headline | ~12 |
| Total unique vocabulary (TF-IDF) | 500 |
| Average named entities per headline | ~2 |
| Total similar pairs found | Thousands |
| Most common entity type | ORG (Organizations) |

---

##  Key Takeaway

The complete pipeline transforms raw text through a structured sequence:

```
Raw Text → Tokens → POS Tags → Named Entities → TF-IDF Vectors → Similarity Scores
```

Each step builds on the previous one, and together they replicate what production NLP systems at major news companies do automatically to organize, tag, and relate thousands of articles every day. Mastering this pipeline is the foundational skill for any NLP or Data Science role.

---

##  File Structure

```
 DAY16/
 ┣  NLP_pipeline.ipynb    
 ┣  cnbc_news_data.csv       
 ┗  README.md                
```
---


