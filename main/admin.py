from django.contrib import admin
from main.models import Meme

class MemeAdmin( admin.ModelAdmin ):
    model = Meme

admin.site.register( Meme, MemeAdmin )

