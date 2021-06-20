from django import forms


class CreateRecipe(forms.Form):
    title = forms.CharField(max_length=30)
    image_url = forms.URLField()
    description = forms.CharField()
    ingredients = forms.CharField(max_length=250)
    time = forms.IntegerField()