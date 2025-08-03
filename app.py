from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quote', methods=['POST'])
def quote():
    make = request.form['make']
    year = request.form['year']
    problem = request.form['problem']

    # Basic quote logic
    base_price = 100
    age_factor = 2025 - int(year)
    quote = base_price + age_factor * 5

    return render_template('quote.html', quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
