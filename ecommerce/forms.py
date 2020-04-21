from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICE = (
    ('S', 'Stripe'),
    ('P', 'paypal')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField()
    apartment_address = forms.CharField(required=False)
    mobile = forms.CharField(max_length=15)
    email = forms.EmailField()
    country = CountryField(blank_label='select country').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))
    state = forms.CharField()
    payment_option = forms.ChoiceField(choices=PAYMENT_CHOICE)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': "Recipient's username",
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4'
    }))
    email = forms.EmailField()
