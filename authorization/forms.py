from django.contrib.auth.forms import AuthenticationForm
from django.forms import ValidationError


class UserEnergyForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.username != 'test' and user.username != 'uaenergy':
            raise ValidationError("You can't login with this account.")
