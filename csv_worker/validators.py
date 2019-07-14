from django.core.validators import ValidationError
from django.utils.translation import gettext as _


def check_type_file(file):
    if ".csv" not in file.name:
        raise ValidationError(_("This is not CSV file. CSV file must contains '.csv' extension."))


def check_size_file(file):
    if file.size > 10 * 1024 ** 2:  # more than 10 MB
        raise ValidationError(_("File size is too big. Input file less that 10 MB."))
