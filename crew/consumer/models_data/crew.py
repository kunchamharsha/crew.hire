from email import charset
from email.quoprimime import unquote
from operator import length_hint
from pydoc import describe
from django.db import models
from .user import User

class Crew(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

class CrewAssets(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    asset_type = models.CharField(
        max_length=15,
        choices=[
            ('images', 'images'),
            ('videos', 'videos'),
            ('gifs', 'gifs'),
            ('documents', 'documents'),
            ('profile_picture', 'profile_picture'),
            ('mast_head', 'mast_head'),
        ],
    )
    url = models.TextField(unique=True)


class CrewUserMapping(models.Model):
    crew = models.ForeignKey(Crew, db_column="crew_id", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, db_column="user_id", on_delete=models.CASCADE
    )
    role = models.CharField(
        max_length=7,
        choices=[
            ('owner', 'owner'),
            ('member', 'member'),
            ('manager', 'manager'),
        ],
    )
