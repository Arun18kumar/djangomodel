from django.forms import ModelForm
from modelapp.models import UserModel 

class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'