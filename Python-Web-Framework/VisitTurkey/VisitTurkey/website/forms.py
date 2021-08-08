from django import forms

from VisitTurkey.website.models import Place, Comment


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = {'user'}

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Name of the place",
            }))

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Enter accurate location",
            }))

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'placeholder': "Enter nice and clear description",
                'rows': "3",
            }))


class CommentForm(forms.ModelForm):
    place_pk = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ('text', 'place_pk')

    def save(self, commit=True):
        place_pk = self.cleaned_data['place_pk']
        place = Place.objects.get(pk=place_pk)
        comment = Comment(text=self.cleaned_data['text'], place=place)

        if commit:
            comment.save()

        return comment
