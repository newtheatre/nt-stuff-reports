from django.urls import include, path 

from . import views 

app_name = 'stuff'
urlpatterns = [

	# Authentication
	#/login
	path('login/', views.stuffLoginView.as_view(), name='stuffLogin'),
	#/logout
	path('logout/', views.stuffLogoutView.as_view(), name='stuffLogout'),

	# Shows 
	path('', views.ShowView.as_view(), name='stuffCurrentShows'),
	path('show/', views.ShowView.as_view(), name='stuffCurrentShows'),
	path('show/all', views.ShowArchiveView.as_view(), name='stuffShowArchive'),
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

	path('log/', views.LogReportListView.as_view(), name='stuffLogList'),
	path('log/<int:pk>/', views.LogReportSingleView.as_view(), name='stuffLogSingle'),
	path('log/<int:pk>/edit', views.LogReportEditView.as_view(), name='stuffLogEdit'),
	path('log/new/', views.LogReportCreateView.as_view(), name='stuffLogNew'),

	path('log/day/', views.DayReportListView.as_view(), name='stuffDayReportList'),
	path('log/day/<int:pk>', views.DayReportView.as_view(), name='stuffDayReport'),
	path('log/day/<int:pk>/edit', views.DayReportEditView.as_view(), name='stuffDayReportEdit'),
	path('log/day/new', views.DayReportCreateView.as_view(), name='stuffDayReportNew'),

	# Festival Reports (TBA)
]
handler404 = views.PageNotFoundView.as_view()