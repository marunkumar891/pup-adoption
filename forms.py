from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class addform(FlaskForm):
	name = StringField('Name of puppy : ')
	submit = SubmitField('Add_Puppy')

class delform(FlaskForm):
	id = IntegerField("Id number of puppy to delete : " )
	submit = SubmitField('Remove puppy')

class addownerform(FlaskForm):
	name = StringField("Enter name of owner : ")
	pup_id = IntegerField("Enter puppy id to adopt : ")
	submit = SubmitField("Add_Owner")
