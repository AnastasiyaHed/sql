from flask import Flask, render_template

app = Flask(__name__)

# Эндпоинты
@app.route('/')
def index():
    return render_template('color.html', color='red')

@app.route('/green')
def green_page():
    return render_template('color.html', color='green')

@app.route('/blue')
def blue_page():
    return render_template('color.html', color='blue')

@app.route('/yellow')
def yellow_page():
    return render_template('color.html', color='yellow')

if __name__ == '__main__':
    app.run(debug=True)

