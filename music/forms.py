from django import forms
from multiupload.fields import MultiFileField


class MusicUploadForm(forms.Form):
    file = forms.FileField()
    
    
class PlaylistCreateForm(forms.Form):
    title = forms.CharField()
    
    def __init__(self, user, *args, **kwargs):
        super(PlaylistCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['tracks'] = forms.ModelMultipleChoiceField(
            queryset = user.tracks.all()
        )