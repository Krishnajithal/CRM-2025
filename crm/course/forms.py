from django import forms

from .models import Course

class AddCourseForm(forms.ModelForm):

    class Meta :

        model  =  Course

        exclude = ['uuid', 'active_status']

        widgets = {

            'code' : forms.TextInput(attrs={'class': "form-control",'required':'required'}),

            'name' : forms.TextInput(attrs={'class': "form-control",'required':'required'}),

            'fee' : forms.TextInput(attrs={'class': "form-control",'required':'required'}),

            'offer_percent': forms.TextInput(attrs={'class': "form-control",'required':'required'}),

            'mode': forms.CheckboxSelectMultiple(attrs={'class': "form-check-input"}),
        }


    # def clean(self):

    #     cleaned_data =  super().clean()

    #     mode = cleaned_data.get('mode')

    #     if mode:

    #         self.add_error('mode','choose atleast one mode')        