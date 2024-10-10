from django import forms

class ExampleForm(forms.Form):
    # Define form fields here
    search_query = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Search...'}),
        help_text="Enter a search term to look for books."
    )
    
    # Add validation methods if needed
    def clean_search_query(self):
        data = self.cleaned_data['search_query']
        # Custom validation can go here (e.g., checking for prohibited characters)
        if len(data) > 100:
            raise forms.ValidationError("Search query is too long.")
        return data
