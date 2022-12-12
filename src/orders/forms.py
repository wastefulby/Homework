from django import forms
from django.contrib.auth.models import User



from . import models


class BookinCartForm(forms.ModelForm):
    class Meta:
        model = models.BookinCart
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'status',
            'phone',
            'name',
            'adress',
            'email',
            'info'
        ]
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.view_order = kwargs.pop('view_order')
        print(self.request.user)
        print(self.view_order)
        super().__init__(*args, **kwargs)
        if self.view_order == True:
            self.fields['status'].widget.attrs['hidden'] = True
        elif self.view_order == False:
            if not self.request.user.is_superuser:
                self.fields['status'].widget.attrs['disabled'] = True
                self.fields['phone'].widget.attrs['disabled'] = True
                self.fields['name'].widget.attrs['disabled'] = True
                self.fields['adress'].widget.attrs['disabled'] = True
                self.fields['email'].widget.attrs['disabled'] = True
                self.fields['info'].widget.attrs['disabled'] = True
        # if self.request.user.is_anonymous:
        #     self.fields['status'].widget.attrs['disabled'] = True            
        #     if self.view_order == True:
        #         del self.fields['status']
        #     else:
        #         self.fields['status'].widget.attrs['disabled'] = True
        #         self.fields['phone'].widget.attrs['disabled'] = True
        #         self.fields['name'].widget.attrs['disabled'] = True
        #         self.fields['adress'].widget.attrs['disabled'] = True
        #         self.fields['email'].widget.attrs['disabled'] = True
        #         self.fields['info'].widget.attrs['disabled'] = True
                