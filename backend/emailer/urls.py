from django.urls import path

from . import views

urlpatterns = [
    path("subscribe/<str:email>", views.NewsletterView.as_view({"post": "subscribe"})),
    path(
        "unsubscribe/<str:email>",
        views.NewsletterView.as_view({"delete": "unsubscribe"}),
    ),
    path(
        "subscriptions",
        views.NewsletterView.as_view({"get": "list_subscribers"}),
    ),
]
