from django.forms import Form, FileField
from .validators import check_type_file, check_size_file


class InputCSV(Form):
    required_css_class = 'form-control-file form-control-lg'

    file = FileField(label="Upload CSV file here...", validators=[check_type_file, check_size_file])
