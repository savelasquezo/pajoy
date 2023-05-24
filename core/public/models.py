from django.db import models
from django.utils.translation import gettext_lazy as _

import datetime

class Tours(models.Model):

    id = models.AutoField(_("ID"),primary_key=True,)
    name = models.CharField(_("Nombre:"), max_length=32,
                                help_text=_("Nombre-Tour (Maximo 32#)"),)
    
    banner = models.ImageField(_("Imagen"), upload_to="uploads/tours/",
        blank=True, null=True, max_length=128, help_text=_("Width 1920px x Height 2190px"),)
    
    location = models.CharField(_("Localizacion:"), max_length=32,
                                help_text=_("Ubicacion (Maximo 32#)"),)
    
    date = models.DateField(_("Fecha:"), default=datetime.date.today,
                                help_text=_("Fecha de Inicio del Tour"),)

    description = models.TextField(_("Comentarios"),
        max_length=256,blank=True,null=True, help_text=_("Descripcion-Tour (Maximo 128#)"),)
    
    price = models.PositiveBigIntegerField(_("Valor"),
        blank=True,default=0, help_text=_("$ ($COP)"),)
    
    online = models.BooleanField(_("¿Activo?"),default=True)

    class Meta:
        verbose_name = _("Tour")
        verbose_name_plural = _("Tours")

    def __str__(self):
        return "Tour: %s" % (self.pk)

class Settings(models.Model):
    
    post1 = models.CharField(_("Nombre:"), max_length=32,
                                help_text=_("Nombre-Tour (Maximo 32#)"),)
    post2 = models.CharField(_("Nombre:"), max_length=32,
                                help_text=_("Nombre-Tour (Maximo 32#)"),)
    post3 = models.CharField(_("Nombre:"), max_length=32,
                                help_text=_("Nombre-Tour (Maximo 32#)"),)

    post1_banner = models.ImageField(_("Imagen-1"), upload_to="uploads/post/",
        blank=True, null=True, max_length=128, help_text=_("Width 720px x Height 730px"),)

    post2_banner = models.ImageField(_("Imagen-2"), upload_to="uploads/post/",
        blank=True, null=True, max_length=128, help_text=_("Width 720px x Height 730px"),)

    post3_banner = models.ImageField(_("Imagen-2"), upload_to="uploads/post/",
        blank=True, null=True, max_length=128, help_text=_("Width 720px x Height 730px"),)
    
    IsActive = models.BooleanField(_("¿Activo?"),default=True)

    class Meta:
        verbose_name = _("Setting")
        verbose_name_plural = _("Settings")

    def __str__(self):
        return "Settings: %s" % (self.pk)