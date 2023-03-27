from flask import Flask, render_template, request
from sympy import *
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post'])
def form():
    if request.method == 'POST':
        equation = str(request.form['equation'])
        f = parse_expr(equation.replace('^', '**').replace('=', '-'),
                       transformations=(standard_transformations + (implicit_multiplication_application,)))
        roots =[r for r in solve(f) if r.is_real]
    return render_template('index.html', roots=roots, equation=equation)


if __name__ == '__main__':
    app.run(debug=True)
