from django import forms
from miApp.models import Producto, Estante

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','precio','fecha_vencimiento')
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'text'}),
        }

class FormEstante(forms.ModelForm):
    class Meta:
        model = Estante
        fields = '__all__'