from django.urls import path
from .views import (AgentListAPIView, GetProfileAPIView,
                    TopAgentListAPIView, UpdateProfileAPIView)


urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path("agents/all/", AgentListAPIView.as_view(), name="all_agents"),
    path("top-agents/all/", AgentListAPIView.as_view(), name="top_agents"),
    path("update/<str:username>/",
         UpdateProfileAPIView.as_view(), name="update_profile"),

]
