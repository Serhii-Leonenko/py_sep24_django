from django.forms.models import inlineformset_factory

from nested_forms.models import Child, Parent

ChildFormset = inlineformset_factory(
    Parent, Child, fields=('name',), extra=1
)


# -------------------------------------adding class to form fields---------------------------------------------------
# class MyForm(forms.Form):
#     myfield = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
# or
# class MyForm(forms.Form):
#     myfield = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
# or
# class MyForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         widgets = {
#             'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
#         }
