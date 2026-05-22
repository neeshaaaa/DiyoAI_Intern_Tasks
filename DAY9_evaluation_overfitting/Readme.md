Breast Cancer Classification using Machine Learning

A machine learning mini project that demonstrates:

Classification using Logistic Regression and Decision Tree
Confusion Matrix visualization
Evaluation Metrics
Overfitting and Generalization concepts

This project is implemented in a Jupyter Notebook (.ipynb) using Python and Scikit-learn.

Project Objectives

The main objectives of this project are:

Understand binary classification problems
Learn how evaluation metrics work
Visualize model performance using confusion matrix
Demonstrate overfitting practically
Compare training and testing accuracy
Dataset Information

This project uses the Breast Cancer Wisconsin Dataset provided by scikit-learn.

Dataset Features
Total Samples: 569
Features: 30 numerical features
Classes:
Malignant (0)
Benign (1)

The dataset is loaded directly using:

from sklearn.datasets import load_breast_cancer

No external CSV file is required.

Technologies Used
Python
Jupyter Notebook
VS Code
Pandas
NumPy
Matplotlib
Scikit-learn
Machine Learning Models Used
1. Logistic Regression

Used as the primary classification model for predicting breast cancer diagnosis.

Purpose
Perform binary classification
Evaluate prediction performance
Generate confusion matrix and metrics
2. Decision Tree Classifier

Used to demonstrate:

Overfitting
Model complexity
Generalization

Two versions were implemented:

Fully grown tree (max_depth=None)
Controlled tree (max_depth=3)
Evaluation Metrics Implemented

The following evaluation metrics were calculated:

Accuracy

Measures overall prediction correctness.

Accuracy = (TP + TN) / (TP + TN + FP + FN)
Precision

Measures how many predicted positives were actually positive.

Precision = TP / (TP + FP)
Recall

Measures how many actual positives were correctly identified.

Recall = TP / (TP + FN)
F1 Score

Harmonic mean of Precision and Recall.

F1 Score = 2 × (Precision × Recall) / (Precision + Recall)
Confusion Matrix

A confusion matrix was used to visualize:

True Positives
True Negatives
False Positives
False Negatives

This helped analyze classification performance more clearly than accuracy alone.

Overfitting Demonstration

The project intentionally created an overfitted Decision Tree model.

Observation
Training accuracy became extremely high
Testing accuracy decreased

This showed that the model memorized training data instead of learning general patterns.

Reducing Overfitting

Overfitting was reduced by limiting tree depth:

DecisionTreeClassifier(max_depth=3)

This improved model generalization on unseen data.

Project Workflow
1. Import Libraries
2. Load Dataset
3. Explore Dataset
4. Train-Test Split
5. Train Logistic Regression Model
6. Evaluate Performance
7. Generate Confusion Matrix
8. Train Decision Tree Model
9. Demonstrate Overfitting
10. Reduce Overfitting
11. Compare Results
Results Summary
Model	Training Accuracy	Testing Accuracy
Logistic Regression	High	High
Decision Tree (Deep)	Very High	Lower
Decision Tree (Limited Depth)	Balanced	Improved
Key Learnings

Through this project, the following concepts were understood practically:

Binary Classification
Train-Test Split
Confusion Matrix
Accuracy
Precision
Recall
F1 Score
Overfitting
Generalization
Model Complexity
Future Improvements


Conclusion

This project successfully demonstrated how machine learning classification models are evaluated using confusion matrices and evaluation metrics. It also showed how overfitting occurs and how controlling model complexity improves generalization performance.

The project provides a strong practical foundation for understanding classification evaluation techniques in machine learning.
