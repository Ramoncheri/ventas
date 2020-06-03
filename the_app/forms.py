from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError


def valida_coste(form, field):
    if field.data>form.precio_unitario.data:
        raise ValidationError('Precio debe ser mayor que el coste')

class ProductForm(FlaskForm): #formulario para validar los datos. Solo hay que definir los datos y ponerle validadores
    id= HiddenField('id')
    tipo_producto = StringField('Tipo de producto', validators= [DataRequired(), Length(min=3, message="Debe tener al menos tres caracteres")])
    precio_unitario= FloatField('Precio U.', validators= [DataRequired()])
    coste_unitario= FloatField('Coste U.', validators=[DataRequired(), valida_coste])

    submit= SubmitField('Aceptar')

# son validaciones en el servidor del formulario

'''
    def validate_coste_unitario(self, field):
        if field.data > self.precio_unitario.data:
            raise ValidationError(' El coste unitario debe ser menor o igual que el precio unitario')
'''