import os
import google.generativeai as genai
from flask import Flask, request, jsonify
import functions_framework

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""
You are a Teaching Assistant Bot.
Explain concepts step by step.
Use simple language and examples.
Stay educational only.
"""
)

flask_app = Flask(__name__)

@flask_app.route("/teach", methods=["POST"])
def teach():
    data = request.json
    user_input = data.get("message", "")
    response = model.generate_content(user_input)
    return jsonify({"reply": response.text})


@functions_framework.http
def app(request):
    return flask_app(request.environ, lambda x, y: None)
