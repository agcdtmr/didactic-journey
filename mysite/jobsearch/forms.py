from django import forms


class FilterJobs(forms.Form):
    job_title = forms.CharField(label="Job Title", max_length=500)
    location = forms.CharField(label="Location", max_length=500, required=False)
    employer_name = forms.CharField(label="Company Name", max_length=500, required=False)
    publication_date = forms.CharField(label="Publication Date", max_length=500, required=False)
    category = forms.CharField(label="Categories", max_length=500, required=False)
