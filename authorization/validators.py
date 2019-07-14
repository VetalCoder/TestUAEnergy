from django.utils.translation import gettext as _


class CheckPassForContainsNeededPassword:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def validate(self, password, user=None):
        if user.username == self.username and password != self.password:
            user.is_active = False
            user.save()

    def get_help_text(self):
        return _("Password in user '{}' broken...").format(self.username)
