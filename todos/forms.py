from django import forms
from todos.models import Todo


class styled_mixing:
    default_classes = "w-full border-2 border-solid border-slate-800 px-2 py-1"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}",
                    'row': 3
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': "border-2 border-solid border-slate-800 px-2 py-1",
                })


class TodoModelForm(styled_mixing, forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {
            'due_date': forms.SelectDateWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
