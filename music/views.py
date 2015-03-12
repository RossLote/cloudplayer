from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from . import forms, models
from django.views.generic import FormView, DetailView, ListView
from django.contrib import messages
from braces import views
from django.http import HttpResponseRedirect

class UserFormView(views.LoginRequiredMixin, FormView):
    
    def get_form(self, form_class):
        """
        Returns an instance of the form to be used in this view.
        """
        return form_class(self.request.user, **self.get_form_kwargs())
    

class TrackListView(views.LoginRequiredMixin, ListView):
    template_name = 'music/track/list.html'
    context_object_name = 'tracks'
    
    def get_queryset(self):
        return self.request.user.tracks.all()
    
    
class LookupListView(views.LoginRequiredMixin, ListView):
    
    def get_queryset(self):
        lookup_field = '{}__id'.format(self.model._meta.model_name)
        lookup_ids = self.request.user.tracks.order_by(
            lookup_field
        # CHANGE FOR POSTGRESQL
        #).distinct(
        #    lookup_field
        ).values_list(
            lookup_field, flat=True
        )
        
        lookup_ids = set(lookup_ids)
        
        return self.model.objects.filter(
            pk__in=lookup_ids
        )
    

class LookupDetailView(TrackListView):
    
    def get_queryset(self):
        lookup_field = '{}__id'.format(self.model._meta.model_name)
        print lookup_field
        print self.kwargs['pk']
        qs = self.request.user.tracks.filter(
            **{
                lookup_field : self.kwargs['pk']
            }
        )
        print qs
        return qs
        


class PlayView(views.LoginRequiredMixin, DetailView):
    context_object_name = 'track'
    
    def get_queryset(self):
        return self.request.user.tracks.all()
    
    def get(self, request, *args, **kwargs):
        return self.get_object().play(request)
    

######################
### UPLOAD ###########
######################

class UploadView(views.LoginRequiredMixin, FormView):
    form_class = forms.MusicUploadForm
    template_name = 'music/upload.html'
    success_url = reverse_lazy('music:upload')
    
    def form_valid(self, form):
        track = models.Track.objects.create_from_file(
            self.request.user, form.cleaned_data['file']
        )
        return super(UploadView, self).form_valid(form)
    
    def form_invalid(self, form):
        return super(UploadView, self).form_valid(form)
    
    
class UploadedView(views.LoginRequiredMixin, ListView):
    template_name = 'music/track/list.html'
    context_object_name = 'tracks'
    
    def get_queryset(self):
        track_ids = self.request.session.get('track_ids', [])
        if track_ids:
            del self.request.session['track_ids']
        queryset = self.request.user.tracks.filter(
            pk__in=track_ids
        )
        return queryset
    
    
######################
### END UPLOAD #######
######################

######################
### PLAYLIST #########
######################
    
class PlaylistCreateView(UserFormView):
    template_name = 'music/playlist/create.html'
    form_class = forms.PlaylistCreateForm
    
    
    def form_valid(self, form):
        cd = form.cleaned_data
        playlist = self.request.user.playlists.create(
            title=cd['title']
        )
        added_tracks = []
        print cd['tracks']
        for i, track in enumerate(cd['tracks']):
            models.PlaylistTrack.objects.create( 
                playlist = playlist,
                track = track,
                sort_order=i
            )
        return HttpResponseRedirect(self.get_success_url(playlist.pk))
    
    def get_success_url(self, playlist_id):
        return reverse('music:playlist-detail', args=[playlist_id])
        

class PlaylistListView(views.LoginRequiredMixin, ListView):
    template_name = 'music/playlist/list.html'
    context_object_name = 'playlists'
    
    def get_queryset(self):
        return self.request.user.playlists.all()
    
    
class PlaylistDetailView(TrackListView):
    
    def get_queryset(self):
        return self.request.user.playlists.get(
            pk=self.kwargs['pk']
        ).tracks.all()

######################
### END PLAYLIST #####
######################

######################
### ALBUM ############
######################

class AlbumListView(LookupListView):
    template_name = 'music/album/list.html'
    context_object_name = 'albums'
    model = models.Album
    

class AlbumDetailView(LookupDetailView):
    model = models.Album
    
######################
### END ALBUM ########
######################

######################
### ARTIST ###########
######################

class ArtistListView(LookupListView):
    template_name = 'music/artist/list.html'
    context_object_name = 'artists'
    model = models.Artist
    

class ArtistDetailView(LookupDetailView):
    model = models.Artist
    
######################
### END ARTIST #######
######################

######################
### ALBUM ############
######################

class GenreListView(LookupListView):
    template_name = 'music/genre/list.html'
    context_object_name = 'genres'
    model = models.Genre
    

class GenreDetailView(LookupDetailView):
    model = models.Genre
    

######################
### END ARTIST #######
######################



