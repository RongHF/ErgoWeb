from django import forms
from django.forms.formsets import formset_factory

class CalForm(forms.Form):
    distance = forms.IntegerField(label="", initial=0, max_value=50, min_value=0)
    load = forms.IntegerField(label="", initial=0, max_value=100, min_value=0)
    rep = forms.IntegerField(label="", initial=100, max_value=5000, min_value=0)


    #damage = forms.FloatField(label="", initial=0.0)
    #damage.widget.attrs['readonly'] = True


    #damage.widget.attrs['disabled'] = True

    #risk = forms.FloatField(label="", initial=0.0)
    #risk.widget.attrs['readonly'] = True
    #risk.widget.attrs['disabled'] = True

class ResultForm(forms.Form):
    damage = forms.FloatField(label="", initial=0)
    damage.widget.attrs['readonly'] = True
    damage.widget.attrs['disabled'] = True
    # damage.widget.attrs['cols'] = 10

    risk = forms.FloatField(label="", initial=0)
    risk.widget.attrs['readonly'] = True
    risk.widget.attrs['disabled'] = True







