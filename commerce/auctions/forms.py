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