from django import template
from datetime import datetime, timedelta, time, date

register = template.Library()

@register.filter
def time_diff(given_time, minutes):
	minutes = int(minutes)
	combination = (datetime.combine(date(1,1,1), given_time) + timedelta(minutes=minutes)).time()
	return combination