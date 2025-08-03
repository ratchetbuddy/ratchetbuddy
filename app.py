from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == 'POST':
        make = request.form['make']
        year = request.form['year']
        problem = request.form['problem']

        # Quote logic
        base_price = 100
        age_factor = 2025 - int(year)
        quote = base_price + age_factor * 5

        return render_template('quote.html', quote=quote)

    return render_template('index.html')  # This shows the form

if __name__ == '__main__':
    app.run(debug=True, port=10000)
