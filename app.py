from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    emoji = str(random.randint(127750, 128751))
    return render_template('index.html', emoji=emoji)

if __name__ == '__main__':
    app.run(debug=True)