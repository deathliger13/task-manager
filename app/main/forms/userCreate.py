from wtforms import Form, StringField, PasswordField, validators, SelectField


class CreateUser(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    role = SelectField(
        'Roles',
        choices=[('manager', 'Manager'), ('dev', 'Developer')]
    )
