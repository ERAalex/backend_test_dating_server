from djoser import email

''' отправка писем при регистрации для Djoser '''


class Activation(email.ActivationEmail):
    template_name = "email/activation.html"


class Confirmation(email.ConfirmationEmail):
    template_name = "email/confirmation.html"
