from flask import Flask, render_template, request
from equation import solve_quadratic

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    roots = solve_quadratic(a, b, c)
    return render_template('result.html', roots=roots)


if __name__ == '__main__':
    app.run()
