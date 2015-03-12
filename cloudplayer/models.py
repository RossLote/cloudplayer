from django.db import models
from django.utils.timezone import now
from django.conf import settings
from os import path
from base64 import b32encode
from sendfile import sendfile
import uuid, os
import hashlib
from mutagen.id3 import ID3
from copy import deepcopy

def get_unique_file_name(filename):
    return b32encode(uuid.uuid4().bytes).strip('=').lower() + '.' + filename.split('.')[-1]

def file_location(instance, filename):
    filename = get_unique_file_name(filename)
    return filename

def write_temp_file(f):
    fn = path.join(settings.TEMP_FILE_ROOT, get_unique_file_name(f.name))
    with open(fn, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return fn

class Tags(object):
    def __init__(self, fn):
        try:
            self._audioinfo = ID3(fn)
        except Exception as e:
            self._audioinfo = {}

        self._load_tags()
        
    def _load_tags(self):
        self._tags = {}
        for key, value in self._audioinfo.iteritems():
            self._tags[key] = value

    def delete(self):
        if self._audioinfo:
            self._audioinfo.delete()

    @property
    def track(self):
        return self._get_attr('TRCK')

    @property
    def title(self):
        return self._get_attr('TIT2')

    @property
    def artist(self):
        return self._get_attr('TPE1')

    @property
    def album(self):
        return self._get_attr('TALB')

    @property
    def image(self):
        apic = self._tags.get('APIC:')
        if apic:
            return apic.data
        return None

    def _get_attr(self, name):
        attr = self._tags.get(name)
        if attr:
            return self._tags.get(name).text[0]
        return None
    

class FileManager(models.Manager):
    def create(self, **kwargs):
        instance = File(**kwargs)
        
        fn = write_temp_file(instance.file)
        
        tags = Tags(fn)
        tags.delete()

        with open(fn, 'r') as temp_file:
            sha = hashlib.sha256(temp_file.read()).hexdigest()
            instance.hash = sha
        try:
            instance.save()
        except Exception as e:
            instance = self.get(hash=sha)

        #os.remove(fn)
        return instance, tags


class File(models.Model):
    hash = models.CharField(max_length=64, unique=True)
    file = models.FileField(upload_to=file_location)
    play_count = models.BigIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    objects = FileManager()
    
    def send(self, request):
        self.play_count+=1
        self.save()
        return sendfile(request, self.get_path())
    
    def get_path(self):
        return '{}/{}'.format(
            settings.MEDIA_ROOT,
            self.file.url
        )