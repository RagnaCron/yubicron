import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


# def validate_even(value):
#     if value % 2 != 0:
#         raise ValidationError(
#             _('%(value)s is not an even number'),
#             params={'value': value},
#         )

def valid_cron_job_syntax(value):
	regex = RegexValidator(
		regex=r'(\*(|[0-5]?[0-9]))\s'           # minutes
		      r'(\*|[01]?\d|2[0-3])\s'          # hours
		      r'(\*|0?[1-9]|[12]\d|3[01])\s'    # days
		      r'(\*|0?[1-9]|1[012])\s'          # months
		      r'(\*|[0-6](\-[0-6])?)'           # day of week
	)



