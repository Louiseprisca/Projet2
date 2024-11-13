from django.contrib import admin
from .models import Feature
from .models import Client
from .models import Réserver
from .models import Compte
from .models import Avis
from .models import Message
from .models import Colis
from .models import Voyage
from .models import Vehicule
from .models import Chauffeur

# Register your models here.
admin.site.register(Feature)
admin.site.register(Client)
admin.site.register(Réserver)
admin.site.register(Compte)
admin.site.register(Avis)
admin.site.register(Message)
admin.site.register(Colis)
admin.site.register(Voyage)
admin.site.register(Vehicule)
admin.site.register(Chauffeur)
