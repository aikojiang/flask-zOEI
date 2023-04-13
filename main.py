from flask import Flask, jsonify
import os

app = Flask(__name__)

openai.api_key = "openai.api_key = "YOUR_API_KEY""

@app.route("/")
def home():
    prompt = "Generate your website content here"
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=100)
    content = response.choices[0].text
    return render_template("index.html", content=content)

if __name__ == "__main__":
    app.run(debug=True)
