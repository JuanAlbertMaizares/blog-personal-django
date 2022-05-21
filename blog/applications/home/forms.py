from django import forms

from .models import Suscribers, Contact

class SuscribersForm(forms.ModelForm):
    class Meta:
        model = Suscribers
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Su correo electronico...'
                }
            ),
        }
class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = ('__all__')

