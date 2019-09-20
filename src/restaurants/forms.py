from django import forms

from restaurants.models import RestaurantLocation
#from restaurants.validators import validate_category


class RestaurantLocationCreateForm(forms.ModelForm):
    #category = forms.CharField(required=False, validators=[validate_category])
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
            'slug',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
