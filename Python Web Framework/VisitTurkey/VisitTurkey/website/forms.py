from django import forms

from VisitTurkey.website.models import Place, Comment


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = {'user'}


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
