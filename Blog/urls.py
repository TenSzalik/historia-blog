from django.contrib import admin
from django.urls import path, include
from wpisy import views as v

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.glowna, name="glowna"),
    path('o_mnie/', v.o_mnie, name="o_mnie"),
    path('wpis/<str:pk>/', v.wpis, name="wpis"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('serce/', v.serce, name="serce"),
]

urlpatterns += [
    path('prehistoria/', v.prehistoria, name="prehistoria"),
    path('starożytność/', v.starożytność, name="starożytność"),
    path('średniowiecze/', v.średniowiecze, name="średniowiecze"),
    path('nowożytność/', v.nowożytność, name="nowożytność"),
    path('współczesność/', v.współczesność, name="współczesność"),
    path('mikrohistoria/', v.mikrohistoria, name="mikrohistoria"),
    path('biografistyka/', v.biografistyka, name="biografistyka"),
    path('drobne-newsy/', v.drobnenewsy, name="drobnenewsy"),
    path('raczek-nieboraczek/', v.raczeknieboraczek, name="raczeknieboraczek"),
    path('filozofia/', v.filozofia, name="filozofia"),
    path('literatura/', v.literatura, name="literatura"),
    path('refleksje/', v.refleksje, name="refleksje"),
    path('psychologia/', v.psychologia, name="psychologia"),
    path('polska/', v.polska, name="polska"),
    path('wynalazki-odkrycia-dzieła/', v.wynalazkiodkryciadzieła, name="wynalazkiodkryciadzieła"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)