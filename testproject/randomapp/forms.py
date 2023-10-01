from django import forms


class ChoiceGameForm(forms.Form):
    game = forms.ChoiceField(choices=[('cube', 'cube'), ('num', 'number'), ('h_or_t', 'heads_or_tails')])
    rolls = forms.IntegerField(min_value=1, max_value=64, widget=forms.NumberInput(attrs={'class': 'form-control'}))
