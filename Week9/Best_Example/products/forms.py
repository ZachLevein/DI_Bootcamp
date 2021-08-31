from django import forms
from .models import Product

## Model Form
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = [
#             'title', 
#             'description',
#             'price'
#         ]


# Raw Django form (1)

# class RawProductForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     price = forms.DecimalField()

# Raw Django form (2)
# Using widgets to fill in the attributes and manipulate how the form fields are structured in the HTML : 

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name", 
                "id:": "my-id-for-textarea",
                "rows": 20,
                "cols" : 120
                }
                )
                )
    price = forms.DecimalField()




# Merging the Raw FORM and the MODEL FORM:
class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

# Validating a specific field on the form so that I can push back a mesage if the condition is True 
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("This is not a valid titile ")
    #     return title