# Naive-Text-Classifier
A simple tool for sentiment analysis and word frequency tracking.

## Features
### 1. Text Preprocessing
- Reads text from a file.
- Cleans punctuation and splits sentences into individual words.

### 2. Sentiment Vocabulary Building
- Uses the API Ninjas Thesaurus API to fetch synonyms for a set of predefined positive and negative words.
- Combines original words and synonyms to create extended positive/negative vocabularies.

### 3. Sentiment Classification
- Counts how many positive and negative words appear in each line of text.
- Classifies each line as Positive, Negative, or Neutral based on word counts.

### 4. Word Frequency Analysis
- Creates a dictionary of word frequencies for all words in the text.
- Identifies the most frequently used words.
- Builds a separate frequency dictionary for words appearing in the positive/negative vocabulary.
