from django.urls import path

from . import views
app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutUsView.as_view(), name='aboutus'),
    path('features', views.FeaturesView.as_view(), name='features'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('signup', views.SignUpView.as_view(), name='sign_up'),
    path('signin', views.SignInView.as_view(), name='signin'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('userregistration', views.UserRegistrationView.as_view(), name='user_registration_view'),
    path('carregistration', views.CarRegistrationView.as_view(), name='car_registration_view'),
    path('rentalcarregistration', views.RentalCarRegistrationView.as_view(), name='rentalcar_registration_view'),

]