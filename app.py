from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from flask_cors import CORS



faq_df = pd.read_csv("custom_postoperative_faq.csv")
questions = faq_df["question"].tolist()
answers = faq_df["answer"].tolist()

#modelo que entende frases e transforma em vetores
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
faq_embeddings = model.encode(questions, show_progress_bar=True)


app = Flask(__name__)
CORS(app)


@app.route("/chat", methods=["POST"])
def chat():
    req_data = request.get_json()
    user_question = req_data.get("message", "")
    if not user_question.strip():
        return jsonify({"response": "Por favor, digite uma pergunta válida."})

    user_embedding = model.encode([user_question])
    similarities = cosine_similarity(user_embedding, faq_embeddings)[0]
    best_idx = np.argmax(similarities)
    best_score = similarities[best_idx]

    threshold = 0.5
    if best_score >= threshold:
        response = answers[best_idx]
    else:
        response = "Desculpe, não entendi sua pergunta. Por favor, consulte seu médico ou reformule."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
