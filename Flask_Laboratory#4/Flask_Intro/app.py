import re
import math
from flask import Flask, render_template, request
from linked_list import LinkedList

app = Flask(__name__)
ll = LinkedList()


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


@app.route('/linked_list', methods=['GET', 'POST'])
def linked_list():
    result = None
    if request.method == 'POST':
        action = request.form.get('action')
        data = request.form.get('data')
        target = request.form.get('target')

        if action == 'insert_beginning' and data:
            ll.insert_at_beginning(data)
            result = f"Inserted {data} at beginning."
        elif action == 'insert_end' and data:
            ll.insert_at_end(data)
            result = f"Inserted {data} at end."
        elif action == 'insert_at' and data and target:
            inserted = ll.insert_at(target, data)
            result = f"Inserted {data} after {target}." if inserted else f"Target {target} not found."
        elif action == 'remove_beginning':
            removed = ll.remove_beginning()
            result = f"Removed {removed} from beginning." if removed else "List is empty."
        elif action == 'remove_end':
            removed = ll.remove_at_end()
            result = f"Removed {removed} from end." if removed else "List is empty."
        elif action == 'remove_at' and data:
            removed = ll.remove_at(data)
            result = f"Removed {removed} from list." if removed else f"Data {data} not found."
        elif action == 'clear_list':
            ll.head = None
            result = "Linked list has been cleared."
        elif action == 'display':
            nodes = ll.display()
            result = " → ".join(ll.display()) if ll.display() else "List is empty."
        elif action == 'search':
            if not data:
                result = "Please enter a value to search."
            else:
                position = ll.search(data)
                if position:
                    result = f"Data '{data}' found at node {position}."
                else:
                    result = f"Data '{data}' not found in the list."


    return render_template('linked_list.html', linked_list=ll.display(), result=result)


if __name__ == '__main__':
    app.run(debug=True)
