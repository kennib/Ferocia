from flask import Flask, request, render_template, flash

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange

from calculations import term_deposit_interest, VALID_PAYMENT_SCHEDULES

app = Flask(__name__)
app.config["SECRET_KEY"] = "Use a ENV Variable in production"
# We don't care about cross site forms here
app.config["WTF_CSRF_ENABLED"] = False

class TermDepositCalculatorForm(FlaskForm):
    deposit = IntegerField('Deposit', default=10000, validators=[DataRequired(), NumberRange(min=0)])
    interest = DecimalField('Interest Rate', default=1.1, places=2, validators=[DataRequired(), NumberRange(min=0, max=10)])
    term = IntegerField('Term', default=3, validators=[DataRequired(), NumberRange(min=1, max=10)])
    schedule = RadioField('Payment Schedule', default="at maturity",
        choices=[
            (schedule, schedule.capitalize())
            for schedule in VALID_PAYMENT_SCHEDULES
        ],
        validators=[DataRequired()])
    submit = SubmitField('Calculate')

@app.route("/",  methods=['GET', 'POST'])
def term_deposit_interest_form():
    form = TermDepositCalculatorForm()

    if form.validate_on_submit():
        final_balance = term_deposit_interest(
            form.deposit.data,
            form.interest.data,
            form.term.data,
            form.schedule.data,
        )
        print(final_balance)
        return render_template('form.html',
            form=form,
            final_balance=f'${final_balance:,}',
        )
    
    if form.errors:
        print(form.errors)
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {field}: {error}")

    return render_template('form.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
