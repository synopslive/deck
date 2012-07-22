# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from markupfield.fields import MarkupField

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    pseudo = models.CharField("Pseudo d'antenne", max_length=30)
    websites = MarkupField("Sites internet (en une ligne)", blank=True, markup_type="markdown")
    description = MarkupField("Description", blank=True, markup_type="markdown")

    avatar = models.ImageField(upload_to='avatars', blank=True)

    is_realname_public = models.BooleanField("Publier son vrai nom sur le site ?", default=False)

    def __unicode__(self):
        return self.pseudo


class Show(models.Model):
    name = models.CharField("Nom du show", max_length=100)
    short = models.CharField("Nom court du show", max_length=25)
    slug = models.SlugField("Slug du show", max_length=30, unique=True)

    description = MarkupField(blank=True, markup_type="markdown")

    podcast_itunes = models.CharField("URL iTunes du podcast", max_length=500, blank=True)
    podcast_rss = models.CharField("URL du RSS du podcast", max_length=500, blank=True)

    icon_image = models.ImageField(upload_to="cartons-ng/shows",
        default="http://synopslive.net/static/medias/cartons-ng/shows/unknown.png",
        blank=True)

    equipe = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

    pass

class Episode(models.Model):
    show = models.ForeignKey(Show)
    number = models.CharField("Numéro de l'épisode", max_length="10")
    time = models.DateTimeField("Date et heure de diffusion")
    termined = models.BooleanField(default=False)

    summary = models.CharField("Resumé de l'émission", max_length=140)
    content = MarkupField("Contenu de l'émission", markup_type="markdown")

    created = models.DateTimeField("Créé en base le", auto_now_add=True)
    modified = models.DateTimeField("Dernière modification le", auto_now=True)

    def visible_downloads(self):
        return self.download_set.filter(visible=True)

    def __unicode__(self):
        return self.show.short + " #" + self.number

    pass

class Download(models.Model):
    episode = models.ForeignKey(Episode)

    name = models.CharField("Type de téléchargement", max_length=30, default="L'émission")
    url = models.CharField("URL du fichier", max_length=500, blank=True)
    visible = models.BooleanField(default=True)

    extension = models.CharField("Extension affichée", max_length=10, default=".mp3", blank=True)
    size = models.CharField("Poids", max_length=10, default="10 Mo", blank=True)

    created = models.DateTimeField("Créé en base le", auto_now_add=True)
    modified = models.DateTimeField("Dernière modification le", auto_now=True)

    def __unicode__(self):
        return u"%s de %s %s" % (self.name, self.episode.show, self.created)

class Carton(models.Model):
    episode = models.ForeignKey(Episode, blank=True)
    standalone = models.BooleanField(default=False)

    published_at = models.DateTimeField(u"Publié le", default=datetime.datetime.now)

    visible = models.BooleanField(u"Affiché en page d'accueil", default=False)

    highlighted = models.BooleanField(u"Affiché au chargement de la page", default=False)

    title = models.CharField("Titre du carton (optionnel)", max_length=255, blank=True)

    bg_image = models.ImageField(upload_to="cartons-ng/fonds",
                                 default="http://synopslive.net/static/medias/cartons-ng/fonds/terrasse.jpg",
                                 blank=True)

    fb_msg = models.CharField("Bouton Facebook", max_length=255,
                              default=u"S'inscrire à l'événement <strong>Facebook</strong>", blank=True)
    fb_url = models.CharField("Lien Facebook", max_length=255, blank=True)

    tw_msg = models.CharField("Bouton Twitter", max_length=255, default="Twitter avec", blank=True)
    tw_url = models.CharField("Lien Twitter", max_length=255, blank=True)

    created = models.DateTimeField(u"Créé en base le", auto_now_add=True)
    modified = models.DateTimeField(u"Dernière modification le", auto_now=True)

    grand_titre = models.CharField("Grand Titre", max_length="255", blank=True)
    tagline = MarkupField(markup_type="markdown", blank=True)

    def __unicode__(self):
        if self.standalone:
            return u"Standalone : %s" % self.title
        else:
            return u"%s" % self.episode + ((u" - %s" % self.title) if self.title else u"")

    pass

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
