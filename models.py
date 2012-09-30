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
        help_text="Cette image sera utilisée comme « icône » sur le site à tous les emplacements.",
        blank=True)

    equipe = models.ManyToManyField(User)

    category = models.ForeignKey("Category", verbose_name="Catégorie", blank=True, null=True, on_delete=models.SET_NULL)

    livepage_url = models.URLField("URL de la page du live",
                                   help_text="Cette URL sera utilisée sur les sites externes, sur les players et sur " \
                                             "le carton pour inviter les internautes à rejoindre le mini-site.",
                                   blank=True, null=True, max_length=255)

    class Meta:
        verbose_name = "show"
        verbose_name_plural = "shows"

    def __unicode__(self):
        return self.name

    pass

class Episode(models.Model):
    show = models.ForeignKey(Show, verbose_name="Show associé")
    number = models.CharField("Numéro de l'épisode", max_length="10",
                             help_text="Numéro (ou indicatif) de l'épisode. Inutile de précéder ce numéro par un « n° » ou « # ».")
    time = models.DateTimeField("Date et heure de diffusion")
    termined = models.BooleanField("Épisode diffusé (terminé)", default=False,
                             help_text="Indique que la diffusion de l'émission est terminée, " \
                                       "et qu'il ne faut plus l'afficher comme « en cours » sur le site. " \
                                       "À cocher systématiquement une fois un épisode effectué.")

    summary = models.CharField("Titre de l'épisode", max_length=140,
                               help_text="Une ligne de texte décrivant l'épisode et le différenciant des autres.")
    content = MarkupField("Contenu de l'épisode", markup_type="markdown",
                         help_text="Ce texte est utilisé dans la page \"Replay\" comme texte d'accompagnement et " \
                                   "de description pour chacune des émissions. Il est pertinent d'y inscrire quelques" \
                                   "paragraphes de texte avec par exemple, la liste des invités ou des participants. " \
                                   "Supporte le Markdown.")

    created = models.DateTimeField("Créé en base le", auto_now_add=True)
    modified = models.DateTimeField("Dernière modification le", auto_now=True)

    specific_livepage_url = models.URLField("URL spécifique de la page du live",
                                            help_text="Vous pouvez laisser ce champ vide ; l'URL habituelle du Live pour " \
                                                      "ce show sera alors utilisée.",
                                            blank=True, null=True, max_length=255)

    class Meta:
        verbose_name = "épisode"
        verbose_name_plural = "épisodes"

    @property
    def livepage_url(self):
        return self.show.livepage_url if not self.specific_livepage_url else self.specific_livepage_url

    def visible_downloads(self):
        return self.download_set.filter(visible=True)

    def __unicode__(self):
        return self.show.short + " #" + self.number

    pass

class Download(models.Model):
    episode = models.ForeignKey(Episode, verbose_name="Épisode associé")

    name = models.CharField("Type de téléchargement", max_length=30, default="L'émission")
    url = models.CharField("URL du fichier", max_length=500, blank=True)
    visible = models.BooleanField(default=True)

    extension = models.CharField("Extension affichée", max_length=10, default=".mp3", blank=True)
    size = models.CharField("Poids", max_length=10, default="10 Mo", blank=True)

    created = models.DateTimeField("Créé en base le", auto_now_add=True)
    modified = models.DateTimeField("Dernière modification le", auto_now=True)

    class Meta:
        verbose_name = "téléchargement"
        verbose_name_plural = "téléchargements"

    def __unicode__(self):
        return u"%s de %s %s" % (self.name, self.episode.show, self.created)

class Carton(models.Model):
    episode = models.ForeignKey(Episode, blank=True)
    standalone = models.BooleanField(default=False)

    published_at = models.DateTimeField(u"Publié le", default=datetime.datetime.now)

    visible = models.BooleanField(u"Affiché en page d'accueil", default=False,
                                  help_text="Si coché, ce carton sera effectivement affiché sur la page d'accueil.")

    highlighted = models.BooleanField(u"Affiché au chargement de la page", default=False,
                                  help_text="Si coché, le carton est « prioritaire »  et affiché en premier dès l'affichage.")

    title = models.CharField("Titre interne du carton (optionnel)", max_length=255, blank=True,
                             help_text="Dans le cas où le carton n'est pas attaché à une émission, remplir ce champ avec " \
                                       "une description de son objet.")

    bg_image = models.ImageField(verbose_name="Image de fond",
                                 upload_to="cartons-ng/fonds",
                                 default="http://synopslive.net/static/medias/cartons-ng/fonds/terrasse.jpg",
                                 blank=True,
                                 help_text="Cette image de fond devrait suivre le " \
                                           "<a href=\"http://www.1mage.net/images/infocarton.png\">patron</a> " \
                                           "pour une plus grande efficacité.")

    fb_msg = models.CharField("Bouton Facebook", max_length=255,
                              default=u"S'inscrire à l'événement <strong>Facebook</strong>", blank=True,
                              help_text="Message affiché sur le bouton Facebook présent sur le carton. HTML autorisé.")
    fb_url = models.CharField("Lien Facebook", max_length=255, blank=True,
                              help_text="URL associée au bouton Facebook. Le bouton Facebook ne sera pas affiché si ce champ est vide.")

    tw_msg = models.CharField("Bouton Twitter", max_length=255, default="Tweeter avec", blank=True,
                              help_text="Message affiché sur le bouton Twitter présent sur le carton. HTML autorisé.")
    tw_url = models.CharField("Lien Twitter", max_length=255, blank=True,
                              help_text="URL associée au bouton Twitter. Le bouton Twitter ne sera pas affiché si ce champ est vide." \
                                        "<br/> Note : il est possible d'utiliser les URLs d'intent Twitter.")

    created = models.DateTimeField(u"Créé en base le", auto_now_add=True)
    modified = models.DateTimeField(u"Dernière modification le", auto_now=True)

    grand_titre = models.CharField("Grand titre", max_length="255", blank=True,
                              help_text="Texte affiché comme titre sur le carton. Il s'agit souvent d'un bon mot ou d'une référence" \
                                        "culturelle pour faire sourire l'auditeur.")

    tagline = MarkupField(verbose_name="Texte du carton", markup_type="markdown", blank=True,
                          help_text="Texte affiché sous le grand titre. Supporte le Markdown.")

    def __unicode__(self):
        if self.standalone:
            return u"Standalone : %s" % self.title
        else:
            return u"%s" % self.episode + ((u" - %s" % self.title) if self.title else u"")

    pass

class LivePage(models.Model):
    show = models.OneToOneField(Show, primary_key=True)

    synopsis = MarkupField(verbose_name="Synopsis", markup_type="markdown", blank=True,
                           help_text="Texte affiché sur la colonne de gauche. Supporte le Markdown.")

    twitter_query = models.CharField("Requête Twitter", max_length=255, default="SynopsLive OR @SynopsLive")

    twitter_button_message = models.CharField("Message par défaut (Twitter)", max_length=255)
    twitter_button_label = models.CharField("Label du bouton Twitter", max_length=255)
    twitter_theme = models.TextField("Thème de Twitter (JSON)", default="{}")

    producer_image = models.CharField("Logo du producteur", max_length=255, blank=True)
    producer_name = models.CharField("Nom du producteur", max_length=255, blank=True, default='SynopsLive')
    producer_url = models.CharField("URL du producteur", max_length=255, blank=True, default='http://synopslive.net')

    top_image = models.CharField("Logo de l'émission (en haut)", max_length=255, blank=True)
    top_link_url = models.CharField("Lien de l'émission (en haut)", max_length=255, blank=True)

    footer = MarkupField(verbose_name="Texte du footer", markup_type="markdown", blank=True,
                         help_text="Texte affiché tout en bas de la page. Supporte le Markdown.")

    css = models.TextField("Style CSS spécifique", default="/* Code CSS ici */")

    def __unicode__(self):
        return u"Page de %s" % self.show

    class Meta:
        verbose_name = "page de direct"
        verbose_name_plural = "pages de direct"

class Category(models.Model):
    name = models.CharField("Nom de la catégorie", max_length=50)
    slug = models.SlugField("Slug de la catégorie", max_length=30, unique=True)
    color = models.CharField("Couleur CSS de la catégorie", max_length=20, default="#CCCCCC")
    icon = models.CharField("URL de l'icône de la catégorie", max_length=255, blank=True)

    class Meta:
        verbose_name = "catégorie"
        verbose_name_plural = "catégories"

    def __unicode__(self):
        return self.name


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
