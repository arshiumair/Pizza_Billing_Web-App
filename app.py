from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    size = request.form.get('size')
    pepperoni = request.form.get('pepperoni')
    cheese = request.form.get('cheese')

    base_price = 0
    pepperoni_price = 0
    cheese_price = 0

    if size == 'S':
        base_price = 15
    elif size == 'M':
        base_price = 20
    elif size == 'L':
        base_price = 25

    if pepperoni == 'Y':
        pepperoni_price = 4 if size == 'S' else 5

    if cheese == 'Y':
        cheese_price = 3

    total = base_price + pepperoni_price + cheese_price

    return render_template(
        'bill.html',
        size=size,
        pepperoni="Yes" if pepperoni == 'Y' else "No",
        cheese="Yes" if cheese == 'Y' else "No",
        base_price=base_price,
        pepperoni_price=pepperoni_price,
        cheese_price=cheese_price,
        total=total
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

