from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.

class PageNotFoundView(generic.ListView):
	template_name = "stuff/404.html"

class ShowView(generic.ListView):
	template_name = "stuff/index.html"
	context_object_name = 'show'
	model = Show 

class CompanyView(generic.DetailView):
	# Show company info, and list shows by company 
	template_name = "stuff/company-detail.html"
	model = Company 

class CompanyListView(generic.ListView):
	template_name = "stuff/company-list.html"
	model = Company 

class RequirementsView(generic.DetailView):
	model = Show
	template_name = 'stuff/requirements-detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['requirement'] = Requirement.objects.filter(show_name=self.object.pk)[0]
		return context

class RequirementsNewView(SuccessMessageMixin, CreateView):
	model = Requirement 
	form_class = RequirementForm 
	template_name = "stuff/forms.html"
	success_message = "Company requirements added"

	def get_success_url(self):
		return reverse_lazy('stuff:stuffRequirements', kwargs={'pk': self.object.pk })

	def get_context_data(self, **kwargs):
		context = super(RequirementsNewView, self).get_context_data(**kwargs)
		context['page_title'] = 'New Requirements list'
		if self.kwargs:
			show_title = Show.objects.filter(pk=self.kwargs['pk'])
			context['report_title'] = 'Add requirements for ' + str(show_title[0])
		else:
			context['report_title'] = context['page_title']
		return context

	def get_initial(self):
		initial = super().get_initial()
		if self.kwargs:
			show_title = Show.objects.filter(pk=self.kwargs['pk'])
			initial['show_name'] = show_title[0]	
		return initial

class RequirementsEditView(SuccessMessageMixin, UpdateView):
	form_class = RequirementForm 
	template_name = "stuff/forms.html"
	success_message = "Edit successful"

	def get_context_data(self, **kwargs):
			context = super(RequirementsEditView, self).get_context_data(**kwargs)
			show_title = Show.objects.filter(pk=self.kwargs['pk'])
			context['report_title'] = 'Edit requirements for ' + str(show_title[0])
			context['page_title'] = 'Edit Requirements'
			return context

	def get_object(self):
		return get_object_or_404(Requirement, show_name=self.kwargs.get(self.pk_url_kwarg))

	def get_success_url(self):
		return reverse_lazy('stuff:stuffRequirements', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg) })

class InductionView(generic.DetailView):
	template_name = "stuff/show-detail.html"
	model = Show

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['induction'] = Induction.objects.filter(show_name=self.object.pk)[0]
		return context

class InductionNewView(SuccessMessageMixin, CreateView):
	model = Induction 
	form_class = InductionForm 
	template_name = "stuff/forms.html"
	success_message = "Company set up!"

	def get_success_url(self):
		return reverse_lazy('stuff:stuffInduction', kwargs={'pk': self.object.pk })

	def get_context_data(self, **kwargs):
		context = super(InductionNewView, self).get_context_data(**kwargs)
		context['page_title'] = 'New Induction'
		if self.kwargs:
			show_title = Show.objects.filter(pk=self.kwargs['pk'])
			context['report_title'] = 'New Induction for ' + str(show_title[0])
		else:
			context['report_title'] = context['page_title']
		return context

	def get_initial(self):
		initial = super().get_initial()
		if self.kwargs:
			show_title = Show.objects.filter(pk=self.kwargs['pk'])
			initial['show_name'] = show_title[0]
		initial['author'] = self.request.user		
		return initial

class InductionEditView(SuccessMessageMixin, UpdateView):
	form_class = InductionForm 
	template_name = "stuff/forms.html"
	success_message = "Edit successful"

	def get_context_data(self, **kwargs):
			context = super(InductionEditView, self).get_context_data(**kwargs)
			show_title = Show.objects.filter(pk=self.kwargs['pk'])
			context['report_title'] = 'Edit ' + str(show_title[0])
			context['page_title'] = 'Edit Show'
			return context

	def get_object(self):
		return get_object_or_404(Induction, show_name=self.kwargs.get(self.pk_url_kwarg))

	def get_success_url(self):
		return reverse_lazy('stuff:stuffInduction', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg) })

class VenueReportView(generic.DetailView):
	template_name = "stuff/report-venue.html"
	model = Show

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['venuereport'] = VenueReport.objects.filter(show_name=self.object.pk)[0]
		return context

class VenueReportNewView(SuccessMessageMixin, CreateView):
	model = VenueReport
	form_class = VenueReportForm 
	template_name = "stuff/forms.html"
	success_message = "Venue report created" 

	def get_success_url(self):
		return reverse_lazy('stuff:stuffVenueReport', kwargs={'pk': self.object.pk })

	def get_context_data(self, **kwargs):
			context = super(VenueReportNewView, self).get_context_data(**kwargs)
			context['page_title'] = 'New Venue Report'
			if self.kwargs:
				show_title = Show.objects.filter(pk=self.kwargs['pk'])
				context['report_title'] = 'New Venue report for ' + str(show_title[0])
			else:
				context['report_title'] = context['page_title']
			return context

	def get_initial(self):
		initial = super().get_initial()
		if self.kwargs:
			show_title = Show.objects.filter(pk=self.kwargs['pk'])
			initial['show_name'] = show_title[0]
		return initial

class VenueReportEditView(SuccessMessageMixin, UpdateView):
	form_class = VenueReportForm
	template_name = "stuff/forms.html"
	success_message = "Edit successful"

	def get_context_data(self, **kwargs):
		context = super(VenueReportEditView, self).get_context_data(**kwargs)
		show_title = Show.objects.filter(pk=self.kwargs['pk'])
		context['report_title'] = 'Edit Venue Report for ' + str(show_title[0])
		context['page_title'] = 'Edit Venue Report'
		return context

	def get_object(self):
		return get_object_or_404(VenueReport, show_name=self.kwargs.get(self.pk_url_kwarg))

	def get_success_url(self):
		return reverse_lazy('stuff:stuffVenueReport', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg) })

class FOHReportView(generic.DetailView):
	template_name = "stuff/report-foh.html"
	model = Show

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['fohreport'] = FOHReport.objects.filter(show_name=self.object.pk)[0]
		return context

class FOHReportNewView(SuccessMessageMixin, CreateView):
	model = FOHReport 
	form_class = FOHReportForm
	template_name = "stuff/forms.html"
	success_message = "Front of House report created"

	def get_success_url(self):
		return reverse_lazy('stuff:stuffFOHReport', kwargs={'pk': self.object.pk })

	def get_context_data(self, **kwargs):
			context = super(FOHReportNewView, self).get_context_data(**kwargs)
			context['page_title'] = 'New FOH Report'
			if self.kwargs:
				show_title = Show.objects.filter(pk=self.kwargs['pk'])
				context['report_title'] = 'New FOH report for ' + str(show_title[0])
			else:
				context['report_title'] = context['page_title']
			return context

	def get_initial(self):
		initial = super().get_initial()
		if self.kwargs:
			show_title = Show.objects.filter(pk=self.kwargs['pk'])
			initial['show_name'] = show_title[0]
		return initial

class FOHReportEditView(SuccessMessageMixin, UpdateView):
	form_class = FOHReportForm
	template_name = "stuff/forms.html"
	success_message = "Edit successful"

	def get_context_data(self, **kwargs):
			context = super(FOHReportEditView, self).get_context_data(**kwargs)
			show_title = Show.objects.filter(pk=self.kwargs['pk'])
			context['report_title'] = 'Edit FOH report for ' + str(show_title[0])
			context['page_title'] = 'Edit FOH Report'
			return context

	def get_object(self):
		return get_object_or_404(FOHReport, show_name=self.kwargs.get(self.pk_url_kwarg))

	def get_success_url(self):
		return reverse_lazy('stuff:stuffFOHReport', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg) })
