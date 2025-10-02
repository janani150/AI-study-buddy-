from flask import Flask, request, jsonify, render_template
from simpleexplanation import explain_topic
from summizer import summarize_text
from prompt import generate_quiz



# create Flask app FIRST
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")




@app.route("/explain", methods=["POST"])
def explain():
    topic = request.json.get("topic")

    return jsonify({"explanation": explain_topic(topic)})




@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json.get("text")

    return jsonify({"summary": summarize_text(text)})




@app.route("/quiz", methods=["POST"])
def quiz():
    text = request.json.get("text")

    return jsonify({"quiz": generate_quiz(text)})




if __name__ == "__main__":
    app.run(debug=True)
