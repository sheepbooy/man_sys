from django import forms


class BootStrapModelForm(forms.ModelForm):
    # 继承ModelForm的类
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class BootStrapForm(forms.Form):
    # 继承MForm的类
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}
