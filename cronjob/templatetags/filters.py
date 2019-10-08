from django import template

register = template.Library()


@register.filter
def intRange(minimum):
	return range(minimum)
