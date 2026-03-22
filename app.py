# app.py
from flask import Flask, request, jsonify
from qa_chain import get_answer

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Question missing!"}), 400

    answer = get_answer(question)
    return jsonify({"answer": answer})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Flask running ✅"})

if __name__ == "__main__":
    print("✅ Flask API running on http://localhost:5000")
    app.run(port=5000, debug=True)
