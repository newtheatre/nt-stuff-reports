import datetime

from django.db import models
from django.utils import timezone 

# Create your models here.

class Venue(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name 

class ShowStop(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Show Stop Trigger"

	def __str__(self):
		return self.name 

class Company(models.Model):
	class Meta:
		verbose_name_plural = "Companies"
	name = models.CharField(
		max_length=250,
		unique=True
	)

	def company_shows(self):
		return Show.objects.filter(company_name=self)

	def __str__(self):
		return self.name 

class Show(models.Model):
	class Meta:
		ordering = ['show_date','performance_start']
	company_name = models.ForeignKey(
		Company,
		on_delete=models.DO_NOTHING
	)

	show_name = models.CharField(max_length=250)

	performance_venue = models.ForeignKey(
		Venue,
		default=None,
		blank=True,
		on_delete=models.DO_NOTHING
	)

	ticketing_id = models.IntegerField(
		unique=True,
		blank=True,
		null=True,
		help_text = 'Go to the <a href="https://ticketing.newtheatre.org.uk/" target="_blank">Ticketing Site</a>, select a show and use the first number in the URL: /SHOWID/0.'
	)

	show_date = models.DateField(blank=True)
	slot_start = models.TimeField(blank=True)
	slot_end = models.TimeField(blank=True)
	performance_start = models.TimeField(blank=True)
	performance_end = models.TimeField(blank=True)

	def has_requirements(self):
		has_requirements = Requirement.objects.filter(show_name=self)
		return has_requirements

	def has_induction(self):
		has_induction = Induction.objects.filter(show_name=self)
		return has_induction

	def has_foh_report(self):
		has_foh_report = FOHReport.objects.filter(show_name=self)
		return has_foh_report

	def has_venue_report(self):
		has_venue_report = VenueReport.objects.filter(show_name=self)
		return has_venue_report

	def __str__(self):
		display_string = '"' + str(self.show_name) + '" by ' + str(self.company_name)
		return display_string

class Requirement(models.Model):
	class Meta:
		verbose_name = "Requirements Form"
		verbose_name_plural = "Requirements Forms"

	show_name = models.OneToOneField(
		Show,
		on_delete = models.CASCADE,
	)
	# Theatre
	using_workshop = models.BooleanField(
		default=False
	)
	using_storage = models.BooleanField(
		default=False
	)
	storage_notes = models.CharField(
		default='None',
		max_length=250,
		help_text = "What is this company bringing to store?",
	)
	using_props = models.BooleanField(default=False)
	prop_notes = models.CharField(
		default='None',
		max_length=250,
		help_text = "What props/costume is this show using from the Theatre?"
	)
	rigging = models.CharField(
		default='None',
		max_length = 250,
		help_text = "Any additional rigging that is required."
	)
	effects = models.CharField(
		default='None',
		max_length=200,
		help_text = "Effects used in this show, eg: strobe, smoke, haze, pyro."
	)
	fire_alarm_disabled = models.BooleanField(default=False)
	theatre_notes = models.TextField(blank=True)

	# Set/Staging
	seating_layout = models.CharField(
		choices = (
			('E', 'End-on'),
			('T', 'Thrust'),
			('R', 'In the round'),
			('O', 'Other (add in notes)'),
		),
		default = 'E',
		max_length = 50
	)
	set_details = models.CharField(
		default='No set',
		max_length=200
	)
	set_notes = models.TextField(blank=True)

	# Tech
	lighting = models.CharField(
		max_length=250,
		default='None',
	)
	sound = models.CharField(
		max_length=250,
		default='None',
	)
	microphones = models.IntegerField(default=0, help_text="How many microphones are being used?")
	video = models.CharField(
		max_length=250,
		default = 'None',
	)
	projector_screen = models.BooleanField(default=False, help_text="Does this show require a projector screen?")
	tech_notes = models.TextField(blank=True)

	def __str__(self):
		display_string = "Requirements form for " + str(self.show_name)
		return display_string

class Induction(models.Model):
	show_name = models.OneToOneField(
		Show,
		on_delete=models.CASCADE, 
	)
	author = models.CharField(
		max_length=100,
		help_text="Who is filling this form out?",
		# Should make this relate to a group of users 
	)
	show_member = models.CharField(
		max_length=100,
		help_text="Who are you speaking to?"
	)
	show_phone = models.IntegerField(
		help_text="What is their phone number?"
	) 
	show_role = models.CharField(
		max_length = 30,
		help_text="What is their role in the company?",
		blank=True
	)
	latecomers = models.CharField(
		max_length = 30,
		help_text = "May latecomers be permitted?",
		choices = (
			('N', 'No latecomers'),
			('Y', 'Latecomers up to the first 15 minutes of the show'),
		),
		default = 'N'
	)
	comps = models.IntegerField(
		default = 0
	)
	comp_list = models.TextField(
		blank=True,
		help_text = "Please list the full names of all people receiving complimentary tickets."
	)
	minimum_audience = models.CharField(
		default='No minimum',
		max_length=255,
		help_text = "Is there a minimum audience to which this company will perform?"
	)

	show_end = models.CharField(
		default='House lights up',
		max_length = 200,
		help_text = "How does the show end? Is this indicated in a certain way?"
	)

	show_stop = models.ManyToManyField(
		ShowStop,
		blank=True,
		help_text="Please indicate the things that <strong>occur during the show</strong>"
	)
	show_stop_notes = models.TextField(
		blank=True,
		help_text="If there are any Show Stop Triggers, provide details about them here."
	)
	shown_spaces = models.BooleanField(
		default=False,
		help_text = "Have you shown the company around the theatre, showing them the areas they can use?"
	)
	performers_pass = models.BooleanField(
		default=False,
		help_text = "Have you informed the company that they can see all the shows today at a discounted rate?"
	)

	timestamp = models.DateTimeField(
		auto_now=True,
	)
	def __str__(self):
		display_string = 'Show Details: ' + str(self.show_name)
		return display_string

class VenueReport(models.Model):
	show_name = models.OneToOneField(
		Show,
		on_delete=models.CASCADE,
	)
	slot_start = models.TimeField(blank=True, null=True)
	get_in_notes = models.TextField(blank=True, null=True)
	house_open = models.TimeField(blank=True, null=True)
	performance_start = models.TimeField(blank=True, null=True)
	performance_notes = models.TextField(blank=True, null=True)
	performance_end = models.TimeField(blank=True, null=True)
	house_clear = models.TimeField(blank=True, null=True)
	get_out_notes = models.TextField(blank=True, null=True)
	slot_end = models.TimeField(blank=True, null=True)
	venue_notes = models.TextField(blank=True, null=True, help_text="General notes")

	def __str__(self):
		display_string = 'Venue Report for ' + str(self.show_name)
		return display_string

class FOHReport(models.Model):
	class Meta:
		verbose_name_plural = "FOH Reports"
		verbose_name = "FOH Report" 

	show_name = models.OneToOneField(
		Show,
		on_delete = models.CASCADE
	)

	audience_behaviour = models.TextField(blank=True)
	foyer_atmosphere = models.TextField(blank=True)

	def __str__(self):
		display_string = 'Front of House report for ' + str(self.show_name)
		return display_string

class DayReport(models.Model):
	class Meta:
		ordering = ['-date']

	date = models.DateField(
		unique=True, 
	)
	auditorium_bar_sales = models.IntegerField(blank=True, null=True)
	studio_bar_sales = models.IntegerField(blank=True, null=True)
	vendor_notes = models.TextField(
		blank=True,
		help_text = "Include each vendor, their day's takings, and any other notes"
	)
	weather = models.CharField(
		blank=True,
		max_length = 200,
	)
	overall_atmosphere = models.TextField(blank=True)
	approx_footfall = models.IntegerField(blank=True, null=True)
	notes = models.TextField(
		blank=True,
		help_text = "Any other points worth noting from the day."
	)

	def __str__(self):
		display_string = 'Day report for ' + str(self.date)
		return display_string

class LogReport(models.Model):
	class Meta:
		ordering = ['-report_date']

	report_type = models.CharField(
		max_length = 50,
		choices = (
			('A', 'Accident'),
			('I', 'Incident'),
			('C', 'Complaint'),
			('N', 'Note'),
		)
	)
	show_name = models.ForeignKey(
		Show, default=None, null=True, blank=True, on_delete=models.CASCADE,
		help_text = "If this log entry is to do with a show, select which one.")
	company_name = models.ForeignKey(
		Company, default=None, null=True, blank=True, on_delete=models.CASCADE,
		help_text = "If this log entry is to do with a company, select which one.")
	author_name = models.CharField(
		max_length=100,
	)
	subject_name = models.CharField(
		max_length=100,
		help_text = "Who, if anyone, is this report about?",
		blank=True,
	)
	report_text = models.TextField(
		help_text = "Festival log entries are only visible to the management team, and will be kept confidential where necessary. Please provide as much detail as possible."
	)
	report_date = models.DateTimeField()

	def __str__(self):
		display_string = str(self.get_report_type_display()) + ' report'
		if self.show_name is not None or self.company_name is not None:
			display_string = display_string + ' about '
			if self.show_name is not None:
				display_string = display_string + str(self.show_name)
			if self.show_name is not None and self.company_name is not None:
				display_string = display_string + ' and '
			if self.company_name is not None:
				display_string = display_string + str(self.company_name)
		display_string = display_string + ' by ' + str(self.author_name)

		return display_string