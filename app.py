from flask import Flask,render_template,request
from transformers import pipeline

app = Flask(__name__)
sentiment_model = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method== "POST":
        text = request.form["review"]
        prediction = sentiment_model(text)
        result=prediction[0]
    return render_template(
        "index.html",
        result=result
    )
if __name__ =="__main__":
    app.run(debug=True)