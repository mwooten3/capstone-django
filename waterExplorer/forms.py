from django import forms
from .models import MaxExtent
import functions

# form for selecting by lake name
class NameForm(forms.Form):
    lake_name = forms.CharField(label = 'Lake Name', max_length = 50)


class SearchForm(forms.Form):

    def get_choice_list(fieldname):
        choices = list([(x, x) for x in MaxExtent.objects.values_list(fieldname, flat=True).distinct() if x != ''])
        choices.insert(0, ('', '-------'))

        return choices

    lake_name = forms.CharField(label = 'Lake Name', max_length = 50, required=False)


    # do not require any field, but be sure one (not 2 or 3) is selected in new clean method below
    country_name = forms.CharField(label = 'Country Name', max_length = 40, required=False) # eventually hopefully be finish text fill in based off country/geoname column contents
    #region_name = forms.ModelChoiceField(label = 'Region Name', required=False, queryset = MaxExtent.objects.values_list('unRegion', flat=True).distinct()) # drop down with options 
#    region_choices = list([(x, x) for x in MaxExtent.objects.values_list('unRegion', flat=True).distinct()])
#    region_choices.insert(0, ('', '-------'))
#    print region_choices
    region_name = forms.ChoiceField(label = 'Region Name', required=False, choices = get_choice_list("unRegion"), widget=forms.Select(attrs={'class': 'form-control'}))#[(x, x) for x in MaxExtent.objects.values_list('unRegion', flat=True).distinct()].insert(0, ('', '-------')))

    subregion_name = forms.ChoiceField(label = 'Subregion Name', required=False, choices = get_choice_list("subregion"), widget=forms.Select(attrs={'class': 'form-control'})) # drop down with options
    continent_name = forms.ChoiceField(label = 'Continent Name', required=False, choices = get_choice_list("continent"), widget=forms.Select(attrs={'class': 'form-control'})) # drop down with options
    size_class = forms.ChoiceField(label = 'Size Range (km^2)', required=False, choices = functions.size_class_tuples(), widget=forms.Select(attrs={'class': 'form-control'})) # fill this out for now, will eventually be drop down of size classes hopefully i.e. 
    water_type = forms.ChoiceField(label = 'Water Body Type', required=False, choices= get_choice_list("typeGlwd"), widget=forms.Select(attrs={'class': 'form-control'})) # will eventually be drop down of options (no selection = all)    

    # override default clean method
    # rules: at least one field has to be filled. the first 4 fields are mutually exclusive
    # can fill one of the first 4 and leave the size/type blank or fill it in as well
    # can also leave first four blank and fill in one or both of the last two
    #* how to deal with this in views? a lot of if's or better way?


    def clean(self):
        cleaned_data = super(SearchForm, self).clean() # use built in clean method first
        country_name = cleaned_data.get("country_name")
        region_name = cleaned_data.get("region_name")
        continent_name = cleaned_data.get("continent_name")
        subregion_name = cleaned_data.get("subregion_name")        
        size_class = cleaned_data.get("size_class")
        water_type = cleaned_data.get("water_type")
        lake_name = cleaned_data.get("lake_name")

        # check to be sure no more than one of the location-based fields is selected
        if (country_name and region_name) or (country_name and continent_name) or (region_name and continent_name) \
         or (country_name and subregion_name) or (region_name and subregion_name) or (continent_name and subregion_name): #* better way to do this?

            raise forms.ValidationError('Please only fill in one of the following fields: Lake Name, Country, Continent, Region, Subregion')

        # check to be sure at least one of the 6 fields is selected
        if not (country_name or region_name or subregion_name or continent_name or size_class or water_type or lake_name): # and 1 of the 6 needs to be selected
            raise forms.ValidationError('Please fill out at least one field') 

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Your message:"
