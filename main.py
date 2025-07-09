from flask import Flask, request, render_template

import locale

from calculations import term_deposit_interest

app = Flask(__name__)

@app.route("/",  methods=['GET', 'POST'])
def term_deposit_interest_form():
    if request.method == 'POST':
        final_balance = term_deposit_interest(
            int(request.form['deposit']),
            float(request.form['interest']),
            int(request.form['term']),
            "at maturity",
        )
        return render_template('form.html', final_balance=f'${final_balance:,.2f}')
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)
