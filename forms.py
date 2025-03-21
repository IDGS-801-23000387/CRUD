from wtforms import Form #type:ignore
from flask_wtf import FlaskForm#type:ignore
 
from wtforms import StringField,IntegerField#type:ignore
from wtforms import EmailField#type:ignore
from wtforms import validators#type:ignore
 
 
class UserForm(Form):
    nombre=StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='ingresa nombre valido')
    ])
    apaterno=StringField('apaterno')
    amaterno=StringField('amaterno')
    email=EmailField('email',[ validators.Email(message='Ingrese un correo valido')])
    edad=IntegerField('edad')
 
 
class UserForm2(Form):
    id=IntegerField('id',
    [validators.number_range(min=1, max=20,message='valor no valido')])
    nombre=StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4,max=20, message='requiere min=4 max=20')
    ])
   
    apaterno=StringField('apaterno',[
        validators.DataRequired(message='El apellido es requerido')
    ])
   
    email=EmailField('correo',[
        validators.DataRequired(message='El apellido es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])