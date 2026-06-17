# 🧠 Mental Health Text Classifier with XAI

An AI-powered web application for analyzing emotional and mental health expressions in text, featuring **Explainable AI (XAI)** visualization using **SHAP** values and a feedback loop stored on a **Supabase** backend.

---

## 🚀 Key Features

* **Hugging Face Model Integration**: Analyzes texts against a fine-tuned Transformers model (`vedabtpatil07/Mental-Health-Analysis`) to classify categories like *Depression*, *Anxiety*, *Suicidal Ideation*, *Positive*, and *Neutral*.
* **Explainable AI (XAI)**: Generates detailed textual and visual SHAP force plots to show exactly which words influenced the prediction (positive or negative impact).
* **Feedback Loop**: Submits user-provided feedback (correctness, corrected labels, and comments) to a Supabase database instance.
* **Modern UI**: Streamlit interface customized with premium linear gradients, modern typography, glassmorphism-style cards, and custom CSS modifications for dark-theme SHAP plots.
* **Custom Dataset**: Trained on a custom dataset created by the author, which is available on Kaggle: [Mental Health Analysis Dataset](https://www.kaggle.com/datasets/anshjaiswal101/mental-health-analysis).

---

## 📁 Project Structure

```text
mental-health-project/
├── notebooks/
│   └── Mental_Health_Analysis.ipynb    # Model training and exploratory analysis notebook
├── app.py                             # Main Streamlit web application
├── requirements.txt                   # Project dependencies
└── README.md                          # Project documentation
```

---

## 🛠️ Setup and Installation

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your system.

### 2. Clone and Configure
Clone this repository to your local directory:
```bash
git clone <repository-url>
cd mental-health-project
```

### 3. Create a Virtual Environment
It is highly recommended to run the app in a virtual environment:
```powershell
# On Windows
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install Dependencies
Install the required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## Run the Application

Start the Streamlit application using:
```bash
streamlit run app.py
```

Once running, navigate to `http://localhost:8501` in your web browser.

---

## 🛡️ Disclaimer

*This tool is intended for research and educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. If you or someone you know is struggling with mental health, please reach out to professional healthcare resources.*
