from django import forms
from .models import Cliente


class Form_creacion_jugador(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class Form_abonos(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configurar el widget para el campo "abono"
        self.fields['abono'].widget = forms.NumberInput(attrs={'class': 'form-control bg-dark text-white mt-3'})
        for field_name, field in self.fields.items():
            if field_name != 'abono':
                field.widget = forms.HiddenInput()
        
