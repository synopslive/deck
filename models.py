# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class EmptyImage:
    def __init__(self):
        pass

    @property
    def url(self):
        return None


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    pseudo = models.CharField("Pseudo d'antenne", max_length=30)
    websites = models.TextField("Sites internet (en une ligne)", blank=True)
    description = models.TextField("Description", blank=True)

    avatar = models.ImageField(upload_to='avatars', blank=True)

    is_realname_public = models.BooleanField("Publier son vrai nom sur le site ?", default=False)

    def __unicode__(self):
        return self.pseudo


class Show(models.Model):
    name = models.CharField("Nom du show", max_length=100)
    short = models.CharField("Nom court du show", max_length=25)
    slug = models.SlugField("Slug du show", max_length=30, unique=True)

    description = models.TextField(blank=True)

    producer = models.ForeignKey("Producer",
                                 verbose_name="Producteur associé",
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 help_text="""
                                 Indique quel est le producteur (entité) est actuellement à l'origine de l'émission.
                                 Cela définiera quel logo sera affiché sur la page de l'émission et la page de direct.
                                 """)

    podcast_itunes = models.CharField("URL iTunes du podcast", max_length=500, blank=True)
    podcast_rss = models.CharField("URL du RSS du podcast", max_length=500, blank=True)

    archived = models.BooleanField("Archivé",
                                   default=False,
                                   help_text="""
                                   Un show archivé n'apparaît pas dans la liste des émissions sur la page d'accueil. <br>
                                   Regroupées alors sous la notion « d'émissions d'archives », les émissions ne devrait
                                   être avoir cette case cochée qu'un mois ou plus après leur dernière émission.
                                   """)

    icon_image = models.ImageField(upload_to="cartons-ng/shows",
                                   default="http://synopslive.net/static/medias/cartons-ng/shows/unknown.png",
                                   editable=False,
                                   help_text="""
                                   DÉPRÉCIÉ : Cette image n'est plus utilisée actuellement sur le site.
                                   """,
                                   blank=True)

    average_duration = models.IntegerField(verbose_name="Durée moyenne, en minutes",
                                           blank=True,
                                           default=60,
                                           help_text="""
                                           Cette donnée est utilisée pour pré-remplir le formulaire de création
                                           d'épisode, et est également affiché sur la page d'émission.
                                           """)

    equipe = models.ManyToManyField(User)

    category = models.ForeignKey("Category", verbose_name="Catégorie", blank=True, null=True, on_delete=models.SET_NULL)

    external_url = models.URLField("URL de la page externe du show",
                                   blank=True,
                                   help_text="""
                                   Si cette URL est indiquée, un bouton sera affiché sur la page d'émission et la
                                   page de direct pour que les auditeurs puissent se rendre sur le micro-site dédié
                                   ou la rubrique chez le producteur.
                                   """)

    external_url_title = models.CharField("Intitulé du lien vers la page externe du show",
                                          blank=False,
                                          max_length=255,
                                          default="Visiter le site dédié à l'émission",
                                          help_text="""
                                          Permet de contextualiser le lien. Le bouton n'est pas affiché si l'URL n'est
                                          pas précisée.
                                          """)

    carton_title = models.CharField("Titre par défaut des cartons",
                                    max_length=255,
                                    blank=True,
                                    help_text="""
                                    Texte affiché en grand sur le carton, par défaut. <br>
                                    Il s'agit traditionnellement d'un bon mot ou d'une référence culturelle
                                    pour faire sourire l'auditeur. <br>
                                    Rappel : les titres ne se terminent jamais par un point simple.
                                    """)

    carton_content = models.TextField(verbose_name="Texte par défaut des cartons",
                                      blank=True,
                                      default="",
                                      help_text="""
                                      Texte affiché sous le titre du carton, par défaut.
                                      Soignez votre orthographe et votre typographie, et n'oubliez pas de vérifier la
                                      taille résultante sur la page d'accueil. <br>
                                      Supporte le Markdown.
                                      """)

    carton_image = models.ImageField(verbose_name="Image par défaut des cartons",
                                     upload_to="cartons-ng/fonds",
                                     blank=True,
                                     default="",
                                     help_text="""
                                     Image de fond du carton qui en donne toute sa couleur et son intensité, par défaut.
                                     La résolution minimale est 1000x500px. Vérifiez que ces proportions sont respectées.
                                     Seule la bande horizontale la plus centrale sera utilisée sur les entêtes de
                                     replay et sur les pages d'émissions.
                                     """)

    livepage_bg_image = models.ImageField(verbose_name="Image de fond du direct",
                                          upload_to="v7/backgrounds/",
                                          default="",
                                          blank=True,
                                          help_text="""
                                              Cette image sera utilisée en fond de la page de direct lorsque le show
                                              est en cours de diffusion. Au besoin, elle peut être écrasée par une
                                              autre image définie au niveau de l'épisode.
                                          """)

    twitter_button_label = models.CharField("Libellé du bouton Twitter",
                                            max_length=255,
                                            blank=True,
                                            default="",
                                            help_text="""
                                            Ce bouton Twitter apparait sur la page de direct, sur la page du show
                                            ainsi que sur la page de l'épisode pour inviter l'auditeur à participer
                                            avec un hashtag. <br>
                                            Si ce champ est vide, le bouton n'est pas affiché.
                                            """)

    twitter_button_message = models.CharField("Message par défaut via Twitter",
                                              max_length=255,
                                              blank=True,
                                              help_text="""
                                              Message pré-rempli par défaut à l'utilisateur au clic sur le
                                              bouton « Tweeter avec... » sur la page de direct. N'oubliez pas
                                              de préciser un hashtag dans le message !
                                              """)

    twitter_widget = models.TextField("Widget Twitter (HTML)", blank=True,
                                      help_text="""
                                      Générez le widget sur <a href="https://twitter.com/settings/widgets">
                                      la page dédiée sur Twitter</a> et collez-le dans ce champ.
                                      """)

    copyright = models.TextField(verbose_name="Footer (copyright)",
                                 blank=True,
                                 help_text="""
                                 Texte affiché en bas des pages d'émissions et sous le texte de l'épisode
                                 sur la page de direct. <br>
                                 Supporte le Markdown.
                                 """)

    class Meta:
        verbose_name = u"émission"
        verbose_name_plural = u"émissions"

    def __unicode__(self):
        return self.name

    pass


class Episode(models.Model):
    show = models.ForeignKey(Show,
                             verbose_name="Émission associée",
                             help_text="""
                             Notez que l'émission contient déjà un carton par défaut et définit des paramètres
                             par défaut pour l'apparence de la page de direct.
                             """)

    number = models.CharField("Numéro de l'épisode",
                              max_length="10",
                              help_text="Numéro (ou indicatif) de l'épisode. Inutile de précéder ce numéro par un « n° » ou « # ».")

    time = models.DateTimeField("Date et heure de diffusion",
                                help_text="""
                                Heure à laquelle l'émission est censée démarrer.
                                À partir de la seconde indiquée, l'émission est considérée comme en cours
                                de lecture sur le player et une notification s'affiche sur la page d'accueil.
                                Cette heure est également utilisée dans la grille des programmes.
                                """)

    end_time = models.DateTimeField("Date et heure de fin de diffusion",
                                    help_text="""
                                    Heure à laquelle l'émission est censée se terminer.
                                    Une fois cette heure dépassée, l'émission sera considérée comme terminée par
                                    le site Internet, les notifications en page d'accueil et le carton associé
                                    disparaîtront, et l'épisode apparaîtra sur le replay.
                                    """)

    summary = models.CharField("Titre de l'épisode",
                               max_length=140,
                               help_text="""
                               Une ligne de texte décrivant l'épisode et le différenciant des autres,
                               utilisée dans la grille des programmes, le résumé en page d'accueil ainsi
                               que sur le replay. <br>
                               Traditionnellement plus simple et sérieux que le titre du carton.
                               """)

    content = models.TextField("Contenu de l'épisode",
                               blank=True,
                               default="",
                               help_text="""
                               Ce texte est utilisé à quatre endroits différents : <br>
                               &nbsp;− sur la page de direct durant l'émission ; <br>
                               &nbsp;− sur la page dédiée à l'épisode ; <br>
                               &nbsp;− sur la page de l'émission, dans la liste des derniers épisodes ; <br>
                               &nbsp;− sur la page de replay, dans la liste des derniers programmes diffusés. <br>
                               Il est pertinent d'y inscrire quelques paragraphes de texte
                               avec par exemple, la liste des invités ou des participants. <br>
                               Supporte le Markdown.
                               """)

    created = models.DateTimeField("Créé en base le",
                                   editable=False,
                                   auto_now_add=True)

    modified = models.DateTimeField("Dernière modification le",
                                    editable=False,
                                    auto_now=True)

    shown = models.BooleanField("Affiché",
                                default=True,
                                blank=None,
                                help_text="""
                                Si cette case est décochée, l'épisode disparaîtra complètement du site,
                                de la grille, et du replay.
                                """)

    carton_title = models.CharField("Titre du carton",
                                    max_length=255,
                                    blank=True,
                                    default="",
                                    help_text="""
                                    Texte affiché en grand sur le carton. Il s'agit traditionnellement d'un bon mot
                                    ou d'une référence culturelle pour faire sourire l'auditeur. <br>
                                    Rappel : les titres ne se terminent jamais par un point simple. <br>
                                    Si ce texte n'est pas rempli, le titre du carton associé à l'émission sera utilisé.
                                    """)

    carton_content = models.TextField(verbose_name="Texte du carton",
                                      default="",
                                      blank=True,
                                      help_text="""
                                      Texte affiché sous le titre du carton.
                                      Soignez votre orthographe et votre typographie, et n'oubliez pas de vérifier la taille
                                      résultante sur la page d'accueil. <br>
                                      Supporte le Markdown. <br>
                                      Si ce texte n'est pas rempli, le texte du carton associé à l'émission sera utilisé.
                                      """)

    carton_image = models.ImageField(verbose_name="Image du carton",
                                     upload_to="cartons-ng/fonds",
                                     max_length=255,
                                     blank=True,
                                     default="",
                                     help_text="""
                                     Image de fond du carton qui en donne toute sa couleur et son intensité.
                                     La résolution minimale est 1000x500px. Vérifiez que ces proportions sont respectées.
                                     Seule la bande horizontale la plus centrale sera utilisée sur les entêtes de
                                     replay et sur les pages d'émissions. <br>
                                     Si aucune image n'est associée, l'image du carton associé à l'émission sera utilisée.
                                     """)

    livepage_bg_image = models.ImageField(verbose_name="Image spécifique de fond du direct",
                                          upload_to="v7/backgrounds/",
                                          default="",
                                          blank=True,
                                          help_text="""
                                              Cette image sera utilisée en fond de la page de direct lorsque l'épisode
                                              est en cours de diffusion. Elle écrase celle définit au niveau de l'émission,
                                              permettant d'avoir des habillages exceptionnels pour certains épisodes.
                                          """)

    priority = models.IntegerField(verbose_name="Priorité",
                                   default=1,
                                   help_text="""
                                   Plus le niveau de priorité est élevé, plus le carton sera affiché en
                                   premier sur la page d'accueil. <br>
                                   Une priorité supérieure à 4 mettera en avant l'émission dans la grille. <br>
                                   Une priorité nulle masque le nom de l'épisode dans la grille : seul le
                                   nom de l'émission est affiché.
                                   """)

    @property
    def auto_carton_image(self):
        if self.carton_image:
            return self.carton_image
        elif self.show.carton_image:
            return self.show.carton_image
        else:
            return EmptyImage()

    @property
    def auto_carton_title(self):
        if self.carton_title:
            return self.carton_title
        elif self.show.carton_title:
            return self.show.carton_title
        else:
            return ""

    @property
    def auto_carton_content(self):
        if self.carton_content:
            return self.carton_content
        elif self.show.carton_content:
            return self.show.carton_content
        else:
            return ""

    @property
    def auto_livepage_bg_image(self):
        if self.livepage_bg_image:
            return self.livepage_bg_image
        elif self.show.livepage_bg_image:
            return self.show.livepage_bg_image
        else:
            return EmptyImage()

    class Meta:
        verbose_name = u"épisode"
        verbose_name_plural = u"épisodes"

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
        verbose_name = u"téléchargement"
        verbose_name_plural = u"téléchargements"

    def __unicode__(self):
        return u"%s de %s %s" % (self.name, self.episode.show, self.created)


class LivePage(models.Model):
    show = models.OneToOneField(Show, primary_key=True)

    synopsis = models.TextField(verbose_name="Synopsis",
                                blank=True,
                                help_text="Texte affiché sur la colonne de gauche. Supporte le Markdown.")

    twitter_button_message = models.CharField("Message par défaut (Twitter)", max_length=255)
    twitter_button_label = models.CharField("Label du bouton Twitter", max_length=255)
    twitter_widget = models.TextField("Widget Twitter (HTML)", blank=True,
                                      help_text="Générez le widget sur <a href=\"https://twitter.com/settings/widgets\"> " \
                                                "la page dédiée sur Twitter</a> et collez-le dans ce champ.")

    producer_image = models.CharField("Logo du producteur", max_length=255, blank=True)
    producer_name = models.CharField("Nom du producteur", max_length=255, blank=True, default='SynopsLive')
    producer_url = models.CharField("URL du producteur", max_length=255, blank=True, default='http://synopslive.net')

    top_image = models.CharField("Logo de l'émission (en haut)", max_length=255, blank=True)
    top_link_url = models.CharField("Lien de l'émission (en haut)", max_length=255, blank=True)

    footer = models.TextField(verbose_name="Texte du footer",
                              blank=True,
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
        verbose_name = u"catégorie"
        verbose_name_plural = u"catégories"

    def __unicode__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField("Nom du producteur", max_length=100,
                            help_text="""
                            Ne créez pas de producteur si celui-ci n'a pas de site Internet. Tout l'intérêt
                            de cet objet est de lier vers un site externe et afficher un logo distinctif.
                            """)
    slug = models.SlugField("Slug du producteur", max_length=50)

    logo = models.ImageField(verbose_name="Logo du producteur",
                             upload_to="v7/producers/",
                             default="",
                             blank=True,
                             help_text="""
                             Affiché sur la page de l'émission et la page de direct, il doit être en monochrome
                             inversé (donc, en blanc et nuance de gris).
                             """)

    external_url = models.URLField("URL du site du producteur")

    regroup_shows = models.BooleanField("Regrouper les émissions",
                                        help_text="""
                                        Regroupe ensemble les émissions de ce producteur. Si cette case est décochée,
                                        le producteur sera toujours affiché sur les pages des différentes émissions
                                        mais il n'apparaîtra pas dans les filtres sur le site. <br>
                                        Cochez cette case s'il s'agit d'un producteur à émission unique sur l'antenne.
                                        """)

    class Meta:
        verbose_name = "producteur"
        verbose_name_plural = "producteurs"

    def __unicode__(self):
        return self.name

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
