from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

class ProductForm(FlaskForm): #formulario para validar los datos. Solo hay que definir los datos y ponerle validadores
    tipo_producto = StringField('Tipo de producto', validators= [DataRequired(), Length(min=3, message="Debe tener al menos tres caracteres")])
    precio_unitario= FloatField('Precio U.', validators= [DataRequired()])
    coste_unitario= FloatField('Coste U.', validators=[DataRequired()])

    submit= SubmitField('Aceptar')

# son validaciones en el servidor