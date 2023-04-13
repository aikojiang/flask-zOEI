from flask import Flask, jsonify
import os

app = Flask(__name__)

openai.api_key = "openai.api_key = ""d8883758-5f2c-4c93-9a2d-d87713f26d0b"""

@app.route("/")
def home():
    prompt = "Generate your website content here"
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=100)
    content = response.choices[0].text
    return render_template("index.html", content=content)

if __name__ == "__main__":
    app.run(debug=True)
