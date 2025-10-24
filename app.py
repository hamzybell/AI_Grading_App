# ==========================================================
# app.py – AI Grading Web Application (Flask Deployment)
# ==========================================================
from flask import Flask, render_template, request, send_file, redirect, url_for
import pandas as pd
import joblib
import os
import re, string
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load saved model and vectorizer
model = joblib.load("ai_grading_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Upload folder for temporary files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------- Helper Functions ----------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def preprocess_data(df):
    df.fillna("", inplace=True)
    df["combined_text"] = (
        df["Equipment"].astype(str)
        + " "
        + df["Procedure"].astype(str)
        + " "
        + df["Result/Output"].astype(str)
        + " "
        + df["Observation/Problem Encountered"].astype(str)
        + " "
        + df["Conclusion"].astype(str)
    )
    df["combined_text"] = df["combined_text"].apply(clean_text)
    return df

# ---------- Routes ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/grade", methods=["POST"])
def grade():
    if "file" not in request.files:
        return redirect(url_for("index"))
    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("index"))

    # Save uploaded CSV
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Load and preprocess data
    df = pd.read_csv(filepath)
    df = preprocess_data(df)

    # Predict scores
    X_vec = vectorizer.transform(df["combined_text"])
    df["Predicted_Total_Score"] = model.predict(X_vec).round(2)

    # Save graded output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(UPLOAD_FOLDER, f"graded_{timestamp}.csv")
    df.to_csv(output_path, index=False)

    # Show preview
    preview = df.head(10).to_html(classes="table table-striped", index=False)

    return render_template("index.html", table=preview, download_link=output_path)

@app.route("/download/<path:filename>")
def download(filename):
    return send_file(filename, as_attachment=True)

# ---------- Run App ----------
if __name__ == "__main__":
    app.run(debug=True)
