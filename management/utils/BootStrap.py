from django import forms


class BootStrapModelForm(forms.ModelForm):
    # 继承ModelForm的类
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 检查字段名称是否为'sales_month'
                if name == 'sales_month':
                    # 为'sales_month'字段应用特定的时间选择插件
                    field.widget.attrs['class'] = 'datepicker_1 form-control'
                else:
                    # 为其他DateField类型字段应用默认的时间选择插件
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
