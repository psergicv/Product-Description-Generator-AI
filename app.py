from flask import Flask, request, render_template, redirect, url_for, session
from openai import OpenAI
from config import app_secret_key, api_key
import os

app = Flask(__name__)
app.secret_key = app_secret_key
#key = os.getenv('OPENAI_API_KEY')
key = api_key
client = OpenAI(
    api_key=key,
    base_url='https://api.together.xyz/v1',
)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def api():
    product_name = request.form['productName']
    style = request.form['style']
    description = description_generator(product_name, style)
    session['description'] = description
    return redirect(url_for('result'))


@app.route('/result')
def result():
    description = session.get('description')
    return render_template('result.html', description=description)


def description_generator(product_name, style):
    style_descriptions = {
        'amuzant': 'amuzanta si hazlie',
        'scurt': 'scurta si clara',
        'lung': 'lunga si detaliata',
        'profesional': 'profesionala'
    }

    prompt_message_system = {
        "role": "system",
        "content": "Tu esti un AI care genereaza descrierea produselor."
    }

    prompt_message_user = {
        "role": "user",
        "content": f"Te rog sa creezi o descriere {style_descriptions[style]} pentru produsul '{product_name}'."
    }

    response = client.chat.completions.create(
        messages=[prompt_message_system, prompt_message_user],
        model="mistralai/Mixtral-8x7B-Instruct-v0.1"
    )

    return response.choices[0].message.content


if __name__ == '__main__':
    app.run()
