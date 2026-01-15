# 🧠 Mental Health Analysis using NLP

An AI-powered mental health text analysis system that detects **Depression, Anxiety, Suicidal Ideation, Happy, and Neutral states** from social media–style text using transformer-based NLP models.

This project focuses on **ethical AI**, **social impact**, and **research-grade NLP**, making it suitable for academic research, MS applications, and AI-for-good initiatives.

---

## 📌 Project Overview

Mental health issues are often expressed subtly through language on social media platforms.  
This project leverages **Natural Language Processing (NLP)** and **transformer-based models** to identify early mental health signals from text data.

### Key Highlights
- Fine-tuned **DistilBERT** for 5-class mental health classification
- Balanced dataset curated from public social media posts
- High performance with **99.5% accuracy**
- Ethical focus with clear limitations and disclaimers
- Deployed-ready with Streamlit frontend

---

## 🏷️ Mental Health Classes

| Label ID | Class Name |
|--------|------------|
| 0 | Depression |
| 1 | Anxiety |
| 2 | Suicidal Ideation |
| 3 | Happy |
| 4 | Neutral / Casual |

---

## 🚀 Model Performance

| Metric | Score |
|------|-------|
| Accuracy | **99.50%** |
| F1-score | **0.995** |
| Precision | **0.995** |
| Recall | **0.995** |
| Loss | **0.0299** |

---

## 🧠 Model & Dataset

- **Base Model**: `distilbert-base-uncased`
- **Framework**: Hugging Face Transformers
- **Dataset**: Balanced 5-class social media dataset  
- **Data Sources**: Public Twitter & Reddit posts (no private data)

🔗 **Hugging Face Model**  
https://huggingface.co/vedabtpatil07/Mental-Health-Analysis

🔗 **Kaggle Dataset**  
https://www.kaggle.com/datasets/anshjaiswal101/mental-health-analysis

---

## 💻 How to Use the Model

### Using Hugging Face Pipeline

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="vedabtpatil07/Mental-Health-Analysis"
)

text = "I feel exhausted and hopeless lately."
result = classifier(text)

print(result)

