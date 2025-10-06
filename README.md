# 🤰 MamaCare - Maternal Health Risk Prediction System

## Overview
MamaCare is an AI-powered maternal health risk prediction system that helps healthcare providers assess and classify maternal health risks into three categories: **Low Risk**, **Mid Risk**, and **High Risk**. The system uses machine learning to analyze clinical parameters and provide real-time risk assessments.

## 🔴 Problem Statement
Maternal mortality remains a critical challenge in healthcare systems worldwide. Early identification of high-risk pregnancies can significantly improve outcomes through timely interventions. MamaCare addresses this by providing:

- Automated risk assessment based on clinical parameters
- Real-time predictions for immediate decision support
- Scalable deployment through cloud infrastructure
- Easy integration with existing healthcare systems

## 📐 Architecture
Data Collection → Data Preprocessing → Model Training → Model Evaluation → Model Serialization
↓                  ↓                   ↓                 ↓                  ↓
(maternal_health.csv)  (Feature       (Random Forest,    (Accuracy,        (model.pkl)
Engineering,    Hyperparameter     Confusion
Data Cleaning,     Tuning,         Matrix,
Train/Test       Cross-Validation) Feature
Split)                          Importance)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/GRACENGARI/mamacare.git
cd mamacare

###installing the dependencies
pip install -r requirements.txt
📊 Dataset
The system uses the maternal_health.csv dataset containing clinical parameters for maternal health assessment.
🤖 Model Details

Algorithm: Random Forest Classifier
Techniques:

Feature Engineering
Hyperparameter Tuning
Cross-Validation


Evaluation Metrics:

Accuracy
Confusion Matrix
Feature Importance
