from django import forms
from home.models  import *
class BookForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={
                            "placeholder":"Your Title",
                            "id":"title",
                            "class":"title-class"
                            }))
    description = forms.CharField(required=False,
                            widget=forms.Textarea(
                                attrs={
                                    "placeholder":"Your Title",
                                    "class":"tittle",
                                    "id":"des",
                                    "row":15,
                                    "cols":100
                                }
                            ))
    price = forms.DecimalField(required=True,initial=100)
    class Meta:
        model = Book
        fields = [
            "title",
            "description", 
            "price"
        ]
    

    # def clean_price(self,*args,**kwargs):
    #     price = self.cleaned_data.get('price')
    #     print(price)
    #     if ( price < 10 ):
    #         print("yes")
    #         raise forms.ValidationError("Price to Low")
    #     else:
    #         print('Nope')