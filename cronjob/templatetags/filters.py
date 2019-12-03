from django import template

register = template.Library()


@register.filter
def int_range(minimum):
	return range(minimum)
