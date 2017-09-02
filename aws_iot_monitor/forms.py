from django 				import forms
from django.core.validators import RegexValidator

# Validator for device searching. Device ID pattern should be like: **alphanumeric
search_validator = RegexValidator(r'^[a-zA-Z0-9]+$')

# Class for device search form
class DeviceSearch(forms.Form):

	devid = forms.CharField(
		max_length=20,
		required=True,
		validators=[search_validator]
	)