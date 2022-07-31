from email import charset
from email.quoprimime import unquote
from operator import length_hint
from pydoc import describe
from django.db import models
from crew.consumer.models_data.user import User

class Crew(models.Model):
    id = models.BigAutoField(primary_key=True, max_length=60)
    name = models.CharField()
    description = models.TextField()

class CrewAssets(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    asset_type = models.enums('images','videos','gifs','documents','profile_picture','mast_head')
    url = models.TextField(unique=True)


class CrewUserMapping(models.Model):
    crew = models.ForeignKey(Crew,db_column="crew_id")
    user = models.ForeignKey(
        User, db_column="user_id", on_delete=models.CASCADE
    )
    role = models.enums('owner','member','manager')
