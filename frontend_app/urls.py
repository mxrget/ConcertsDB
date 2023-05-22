from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name='home'),
    path("/", views.MainPageView.as_view(), name='home-1'),
    path("home/", views.MainPageView.as_view(), name='home-2'),
    path("about", views.AboutView.as_view(), name='about'),
    path("search", views.SearchView.as_view(), name='search'),
    path("all-events", views.AllEventsView.as_view(), name='all-events'),
    path("event-<int:pk>/", views.EventDetailView.as_view(), name='event-detail'),
    path("performer-<int:pk>/", views.PerformerView.as_view(), name='performer-detail'),
]
