import re
import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    error = None
    if request.method == 'POST':
        s = request.form.get('inputString', '').strip()
        if not s:
            error = "Please enter a value before converting."
        elif not re.fullmatch(r'[A-Za-z]+', s):
            error = "Only letters A–Z are allowed."
        else:
            result = s.upper()
    return render_template('touppercase.html', result=result, error=error)

@app.route('/area_circle', methods=['GET', 'POST'])
def area_circle():
    area = None
    error = None
    if request.method == 'POST':
        r_raw = request.form.get('radius', '').strip()
        if not r_raw:
            error = "Please enter a radius before calculating."
        else:
            try:
                radius = float(r_raw)
                if radius < 0:
                    error = "Please enter a non-negative radius."
                else:
                    area = math.pi * radius * radius
            except ValueError:
                error = "Please enter a valid number for radius."
    return render_template('area_circle.html', area=area, error=error)

@app.route('/area_triangle', methods=['GET', 'POST'])
def area_triangle():
    area = None
    error = None
    if request.method == 'POST':
        base_raw = request.form.get('base', '').strip()
        height_raw = request.form.get('height', '').strip()

        if not base_raw or not height_raw:
            error = "Please enter both base and height before calculating."
        else:
            try:
                base = float(base_raw)
                height = float(height_raw)
                if base < 0 or height < 0:
                    error = "Please enter valid non-negative numbers for base and height."
                else:
                    area = 0.5 * base * height
            except ValueError:
                error = "Please enter valid numbers for base and height."
    return render_template('area_triangle.html', area=area, error=error)

if __name__ == '__main__':
    app.run(debug=True)