from django.contrib import admin, messages
from django.db import models
from .models import * 
from django.forms import CheckboxSelectMultiple

# Register your models here.

class ShowAdmin(admin.ModelAdmin):
	fieldsets = (
		(None,{
			'fields': (
				('company_name',
				'show_name'),
				'performance_venue',
				'ticketing_id',
			),
		}),
		('Dates and Times',{ 
			'fields': (
				'show_date',
				('slot_start', 'slot_end'),
				('performance_start', 'performance_end'),
			),
		}),
	)
	list_display = ('show_name','company_name','show_date','performance_venue','performance_start', 'performance_end')

class RequirementAdmin(admin.ModelAdmin):
	fieldsets = (
		(None,{
			'fields': (
				'show_name',
			),
		}),
		('Theatre',{
			'fields': (
				'using_workshop',
				('using_storage','storage_notes'),
				('using_props', 'prop_notes'),
				'rigging',
				('effects','fire_alarm_disabled'),
				'theatre_notes',
			)
		}),
		('Set / Staging', {
			'fields': (
				'seating_layout',
				'set_details',
				'set_notes'
			)
		}),
		('Technical', {
			'fields': (
				'lighting',
				'sound',
				'video',
				'tech_notes'
			),
		}),
	)

class InductionAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}

class VenueReportAdmin(admin.ModelAdmin):
	fieldsets = (
		(None,{
			'fields': (
				'show_name',
				'venue_notes',
			)
		}),
		('Get In', {
			'fields': (
				'slot_start',
				'get_in_notes',
				'house_open',
			)
		}),
		('Show', {
			'fields': (
				'performance_start',
				'performance_end',
				'performance_notes',
			)
		}),
		('Get Out', {
			'fields': (
				'house_clear',
				'slot_end',
			)
		})
	)

admin.site.register(Venue)
admin.site.register(Company)
admin.site.register(Show, ShowAdmin)
admin.site.register(Induction, InductionAdmin)
admin.site.register(VenueReport, VenueReportAdmin)
admin.site.register(FOHReport)
admin.site.register(LogReport)
admin.site.register(DayReport)
admin.site.register(ShowStop)
admin.site.register(Requirement, RequirementAdmin)