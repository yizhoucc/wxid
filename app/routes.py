from flask import render_template, flash, redirect, url_for
from app import app, dbconnector, db
from app.forms import SearchForm, InputForm
''''''
''''''

mydb=dbconnector.connect2db()
# cursor is created each operation


@app.route('/search', methods=['GET', 'POST'])
def search():
    # flash('search')
    form = SearchForm()
    if form.validate_on_submit():
        # do xx xhere to sql
        data=db.searchdb(form, mydb)
        flash('恭喜 操作成功')
        flash(data)

    return render_template('search.html',  title='2 In', form=form)

@app.route('/input', methods=['GET', 'POST'])
def inputdata():
    # flash('input')
    form = InputForm()
    if form.validate_on_submit():
        # do xx xhere to sql
        data=db.insertion(form, mydb)
        flash('恭喜, 操作成功')
        flash(data)


    return render_template('input.html',  title='3 In', form=form)

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('base.html',  title='1 In')