from django import forms 
from .widgets import CustomTimePicker
from stuff.models import *

class RequirementForm(forms.ModelForm):
	class Meta:
		model = Requirement 
		fields = '__all__'

class InductionForm(forms.ModelForm):
	class Meta:
		model = Induction 
		fields = '__all__'
		exclude = {
			'timestamp'
		}
		widgets = {
			'show_phone': forms.widgets.TextInput(),
				## TODO: Don't strip starting 0
			'show_stop': forms.widgets.CheckboxSelectMultiple(),
		}

	# show_name = Show.objects.filter(has_induction is not None)
	# Change field.show_name to be Show.objects.filter(has_induction=False)
	# Set field.show_name to be read-only when editing (as below, potentially)
			# def __init__(self, *args, **kwargs):
			#     request = kwargs.pop("request", None)
			#     super(FOHReportForm, self).__init__(*args, **kwargs)
			#     instance = getattr(self, 'instance', None)
			#     if instance and instance.pk:
			#         self.fields.pop('show_name')

class VenueReportForm(forms.ModelForm):
	class Meta:
		model = VenueReport 
		fields = '__all__'
		exclude = { 'timestamp '}

	# Make the timepicker appear for all time-based fields automagically 
	def __init__(self, *args, **kwargs):
		super(VenueReportForm, self).__init__(*args, **kwargs)
		for key, value in self.fields.items():
			if key in ['slot_start', 'house_open', 'performance_start', 'performance_end',
			'house_clear', 'slot_end']:
				self.fields[key].widget = CustomTimePicker()

class FOHReportForm(forms.ModelForm):
	class Meta:
		model = FOHReport 
		fields = '__all__'
		exclude = { 'timestamp '}

class LogReportForm(forms.ModelForm):
	class Meta:
		model = LogReport  
		fields = '__all__'
		exclude = { 'report_date' }