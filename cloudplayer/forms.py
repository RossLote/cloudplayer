from django import forms
from multiupload.fields import MultiFileField

class FileUploadForm(forms.Form):
    files = MultiFileField(max_num=100, min_num=1, max_file_size=1024*1024*5)