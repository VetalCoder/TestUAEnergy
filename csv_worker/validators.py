from django.core.validators import ValidationError


def check_type_file(file):
    if ".csv" not in file.name:
        raise ValidationError("This is not CSV file. CSV file must contains '.csv' extension.")


def check_size_file(file):
    if file.size > 10 * 1024 ** 2:  # more than 10 MB
        raise ValidationError("File size is too big. Input file less that 10 MB.")
