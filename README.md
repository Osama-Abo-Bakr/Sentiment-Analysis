# Sentiment Analysis Project

## Overview

This project focuses on building a sentiment analysis model using two popular machine learning algorithms: **Naive Bayes** and **Random Forest**. The goal is to classify text data (reviews) as either positive or negative, and the model is deployed using Streamlit for real-time sentiment prediction.

## Table of Contents

1. [Project Description](#project-description)
2. [Data](#data)
3. [Preprocessing](#preprocessing)
4. [Feature Extraction](#feature-extraction)
5. [Modeling](#modeling)
6. [Evaluation](#evaluation)
7. [Deployment](#deployment)
8. [How to Run](#how-to-run)
9. [Contributing](#contributing)
10. [License](#license)

## Project Description

Sentiment analysis is a powerful technique used to determine the sentiment of text data, such as reviews or social media posts. This project leverages **Naive Bayes** and **Random Forest** classifiers to create models that can accurately predict whether a review is positive or negative.

The project is divided into several key stages, including data preprocessing, feature extraction, model training, and deployment. The resulting models were evaluated for their performance, and the best model was deployed using Streamlit.

## Data

The dataset used in this project consists of restaurant reviews, which are labeled as either "Liked" (1) or "Not Liked" (0). The data is preprocessed to remove noise and irrelevant information before being used to train the models.

## Preprocessing

The preprocessing steps involved:

- **Text Lowercasing:** Converting all text to lowercase.
- **Removing Punctuation:** Eliminating punctuation marks from the text.
- **Stopwords Removal:** Removing common English stopwords that do not contribute to sentiment.
- **Lemmatization:** Reducing words to their base form.

These steps ensure that the text data is clean and ready for feature extraction.

## Feature Extraction

Two methods were used for feature extraction:

1. **TF-IDF (Term Frequency-Inverse Document Frequency):** Captures the importance of words in the corpus.
2. **Bag of Words:** Represents the text data as a matrix of token counts.

Both methods were used to create features for model training.

## Modeling

Two models were trained:

1. **Naive Bayes Classifier:**
   - Used both TF-IDF and Bag of Words features.
   - Evaluated on training and testing sets.

2. **Random Forest Classifier:**
   - Also trained using TF-IDF and Bag of Words features.
   - Provided more robust performance due to its ensemble nature.

## Evaluation

The models were evaluated based on accuracy scores on both training and testing datasets. The Random Forest model using TF-IDF features achieved the best performance and was chosen for deployment.

## Deployment

The best-performing model was deployed using **Streamlit**, a popular Python library for creating interactive web applications. Users can input text and receive real-time sentiment predictions.

## How to Run

To run the project locally:

1. !git clone https://github.com/Osama-Abo-Bakr/Sentiment-Analysis
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the Streamlit app with the command `streamlit run app.py`.


'''bash
!git clone https://github.com/Osama-Abo-Bakr/Sentiment-Analysis
cd imdb-review-sentiment-analysis
'''
'''bash
streamlit run app.py
'''


## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
