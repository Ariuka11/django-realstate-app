from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.ListAllPropertiesAPIView.as_view(), name="all-properties"),
    path("agents/", views.ListAgentsPropertiesAPIView.as_view(), name="all-agents"),
    path("create/", views.create_property_api_view, name="property-create"),
    path("details/", views.PropertyDetailView.as_view(), name="property-detail"),
    path("update/", views.update_property_api_view, name="property-update"),
    path("delete/", views.delete_property_api_view, name="property-delete"),
    path("search/", views.PropertySearchAPIView().as_view(), name="property-search"),
]
