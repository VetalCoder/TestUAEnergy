from django.forms import Form, FileField
from .validators import check_type_file, check_size_file
from django.utils.translation import gettext_lazy as _


class InputCSV(Form):
    required_css_class = 'form-control-file form-control-lg'

    file = FileField(label=_("Upload CSV file here..."), validators=[check_type_file, check_size_file])
