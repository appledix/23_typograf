from flask import Flask, render_template, request
from typographer import prepare_text_for_publication

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        formatted_text = prepare_text_for_publication(request.form['text'])
        return render_template('form.html', result=formatted_text)
    else:
        return render_template('form.html')

if __name__ == "__main__":
    app.run()
