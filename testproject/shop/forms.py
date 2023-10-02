from django import forms


class AddNewProduct(forms.Form):
    product_name = forms.CharField(max_length=200)
    description = forms.CharField()
    price = forms.FloatField(min_value=0.0)
    quantity = forms.IntegerField(min_value=0)
    product_image = forms.ImageField()
