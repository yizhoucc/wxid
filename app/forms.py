from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):

    # 1st part
    wxid = StringField('Enter his/her Wechat ID', validators=[DataRequired()])
    lastname = StringField('Enter his/her Last Name in English', validators=[DataRequired()])
    submit = SubmitField('search now')

class InputForm(FlaskForm):

    # 2nd part
    mywxid=StringField('Enter your Wechat ID', validators=[DataRequired()])
    mylname= StringField('Enter your Last Name in English', validators=[DataRequired()])
    app1=StringField('App name', validators=[DataRequired()])
    id1=StringField('id number friend code', validators=[DataRequired()])
    app2=StringField('App name')
    id2=StringField('id number friend code')
    app3=StringField('App name')
    id3=StringField('id number friend code')
    submit2 = SubmitField('build your record now')


