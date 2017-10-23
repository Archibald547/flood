from registration.backends.simple.views import RegistrationView
from .forms import ProfileForm
from .models import MyProfile



class MyRegistrationView(RegistrationView):


    form_class = ProfileForm


    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        f_name = form_class.cleaned_data['first_name']
        l_name = form_class.cleaned_data['last_name']
        l = form_class.cleaned_data['location']
        b_date = form_class.cleaned_data['birth_date']
        b = form_class.cleaned_data['bio']

        new_profile = MyProfile.objects.create(user=new_user, first_name=f_name, last_name=l_name, location = l, birth_date=b_date, bio=b)
        new_profile.save()
        return new_user

    def get_success_url(self, user):
        return "/"

