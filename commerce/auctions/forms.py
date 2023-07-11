from django import forms


# add new listing
class NewListing(forms.Form):
    title = forms.CharField(label="Title",
                            required=True
                            )
    description = forms.CharField(
        widget = forms.Textarea( attrs={"rows":"5"} ),
        required= True
    )
    bid = forms.IntegerField(
        min_value=0, 
        max_value=32767, 
        required=True, 
        label="initial bid"
	)
    image = forms.URLField(label="URL to product image", required=False)
    category = forms.CharField(label="Categories", required=False)
    

class NewComment(forms.Form):
    stars = forms.IntegerField(min_value=1, max_value=5, label="Starts")
    comment = forms.CharField(label="Describe your thougths")
    owner = forms.CharField(required=True)
    listing = forms.IntegerField(required=True)