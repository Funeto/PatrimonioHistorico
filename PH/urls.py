from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from PC.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='url_index'),
    path('login/', login, name="url_login"),
    path('createPatrimonio/', createP, name='url_createP'),
    path('showPatrimonio/<int:id>', showP, name='url_showP'),
    path('readPatrimonio/', readP, name='url_readP'),
    path('deletePatrimonio/<int:id>', delP, name='url_delP'),
    path('updatePatrimonio/<int:id>', updateP, name='url_updateP'),
    path('deleteComentario/<int:idp>/<int:idc>', delC, name='url_delC'),
    path('adminUsuario/', adminU, name='url_adminU'),
    path('createUsuario/',createU, name='url_createU'),
    path('showUsuario/', showU, name='url_showU'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)