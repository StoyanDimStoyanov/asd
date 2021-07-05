from django.urls import path

from demo.views import UserDetailsApiView

urlpatterns = [
    path('create/', UserDetailsApiView.as_view())

]