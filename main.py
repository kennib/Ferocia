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
            request.form['schedule'],
        )
        return render_template('form.html',
            deposit=int(request.form['deposit']),
            interest=float(request.form['interest']),
            term=int(request.form['term']),
            schedule=request.form['schedule'],
            final_balance=f'${final_balance:,.2f}',
        )
    else:
        return render_template('form.html',
            deposit="10000",
            interest="1.10",
            term="3",
            schedule="at maturity",
        )


if __name__ == "__main__":
    app.run(debug=True)
