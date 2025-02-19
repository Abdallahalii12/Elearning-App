from django.urls import path
from .views import sign_up,sign_out,sign_in,view_profile,edit_profile
app_name = 'accounts'  # Defines the namespace

# Temporary views to prevent errors
urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('sign-out/', sign_out, name='sign_out'),
    path('sign-in/', sign_in, name='sign_in'),
    path('view-profile/',view_profile,name='view_profile'),
    path('edit-profile/',edit_profile,name='edit_profile'),
]
