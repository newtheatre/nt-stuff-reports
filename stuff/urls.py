from django.urls import include, path 

from . import views 

app_name = 'stuff'
urlpatterns = [

	path('', views.ShowView.as_view(), name='stuffCompanies'),
	path('show/', views.ShowView.as_view(), name='stuffCompanies'),
	path('show/<int:pk>/', views.InductionView.as_view(), name='stuffInduction'),
	path('show/<int:pk>/', include([
		path('start/', views.InductionNewView.as_view(), name='stuffInductionNew'),
		path('edit/', views.InductionEditView.as_view(), name='stuffInductionEdit'),
		path('requirements/', views.RequirementsView.as_view(), name='stuffRequirements'),
		path('requirements/new', views.RequirementsNewView.as_view(), name='stuffRequirementsNew'),
		path('requirements/edit', views.RequirementsEditView.as_view(), name='stuffRequirementsEdit'),
		path('venue/', views.VenueReportView.as_view(), name='stuffVenueReport'),
		path('venue/new', views.VenueReportNewView.as_view(), name='stuffVenueReportNew'),
		path('venue/edit', views.VenueReportEditView.as_view(), name='stuffVenueReportEdit'),
		path('foh/', views.FOHReportView.as_view(), name='stuffFOHReport'),
		path('foh/new', views.FOHReportNewView.as_view(), name='stuffFOHReportNew'),
		path('foh/edit', views.FOHReportEditView.as_view(), name='stuffFOHReportEdit'),
	])),

	path('company/<int:pk>', views.CompanyView.as_view(), name='stuffCompanySingle'),

	path('requirements', views.RequirementsNewView.as_view(), name='stuffRequirementsBlankNew'),
	path('induction', views.InductionNewView.as_view(), name='stuffInductionBlankNew'),
	path('venue', views.VenueReportNewView.as_view(), name='stuffVenueReportBlankNew'),
	path('foh', views.FOHReportNewView.as_view(), name='stuffFOHReportBlankNew'),
	
	# Festival Reports (TBA)
	# Daily Reports		 (TBA)
]
handler404 = views.PageNotFoundView.as_view()