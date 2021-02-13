from django.urls import path
from jobs.api.views import JobOfferDetailCreateAPIView, JobOfferListCreateAPIView

urlpatterns = [
  path("jobs/", JobOfferListCreateAPIView.as_view(), name="job-list"),
  path("jobs/<int:pk>", JobOfferDetailCreateAPIView.as_view(), name="job-detail")
]