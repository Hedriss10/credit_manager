from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Credit, db
from .forms import CreditForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    credits = Credit.query.all()
    return render_template('index.html', credits=credits)

@main.route('/add', methods=['GET', 'POST'])
def add_credit():
    form = CreditForm()
    if form.validate_on_submit():
        new_credit = Credit(client_name=form.client_name.data, credit_amount=form.credit_amount.data)
        db.session.add(new_credit)
        db.session.commit()
        flash('Credit request added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('credit.html', form=form)

@main.route('/approve/<int:credit_id>')
def approve_credit(credit_id):
    credit = Credit.query.get_or_404(credit_id)
    credit.approve()
    flash(f'Credit request for {credit.client_name} approved!', 'success')
    return redirect(url_for('main.index'))
