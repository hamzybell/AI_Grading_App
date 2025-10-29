# 🧠 AI-Based Automated Grading System for Computer Science Practical Reports  
**Case Study: Open, Distance and Flexible e-Learning (ODFeL) Students – Yaba College of Technology, Nigeria**  

## 📘 Project Overview  
This project implements an AI-powered system for **automated grading of computer science practical reports** using Natural Language Processing (NLP) and Machine Learning (ML).  
It was developed as a **capstone project** by **Bello Afsat Bola**, Department of Computer Science, Yaba College of Technology, Nigeria.  

The system automatically evaluates students’ practical reports based on well-defined rubrics, improving the efficiency, objectivity, and consistency of assessment in large-class environments.  

---

## ⚙️ Features  
- Upload student practical reports in CSV format.  
- Automatic grading using a trained Machine Learning model.  
- Download graded results instantly.  
- Simple and intuitive Flask-based web interface.  
- Deployed online via Render for real-time access.  

---

## 🧮 Scoring Rubric (20 Marks)
| Criterion | Max Marks | Description |
|------------|------------|--------------|
| Equipment | 4 | Accuracy and completeness of equipment listed. |
| Procedure | 5 | Clarity and correctness of practical steps. |
| Result/Output | 7 | Correctness and explanation of outcomes. |
| Observation/Problem Encountered | 2 | Relevance and clarity of noted issues. |
| Conclusion | 2 | Reflection and logical summary of the experiment. |

---

## 🌍 Live Application  
🔗 **Access the deployed system here:**  
👉 [https://ai-grading-system.onrender.com](https://ai-grading-system.onrender.com)

---

## 🧰 Technologies Used  
- **Python (Flask Framework)** – Web interface and backend logic  
- **Pandas & Scikit-learn** – Data preprocessing and machine learning  
- **Joblib** – Model serialization  
- **HTML, CSS (Bootstrap)** – Web user interface  
- **Gunicorn** – Production-grade web server for deployment  
- **Render.com** – Cloud hosting and CI/CD deployment  

---

## 🧠 Model Information  
- Dataset size: **7,500+ student practical reports** (2,720 labeled for training).  
- Algorithms tested: **Naïve Bayes, SVM, Decision Tree, Random Forest**.  
- Final model: **RandomForestRegressor** trained on TF-IDF text features.  
- Evaluation metrics: **Mean Absolute Error (MAE), R² Score, Grading Consistency**.  

---

## 🏗️ System Architecture  
