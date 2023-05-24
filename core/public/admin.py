from django.contrib import admin
import public.models as model


class MyAdminSite(admin.AdminSite):
    index_title = 'Panel Administrativo'
    verbose_name = "PAJOY-TOURS"


    def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site. NewMetod for ordering Models
        """
        ordering = {"Usuarios": 1, "Tours": 2, "Settings": 3,}
        app_dict = self._build_app_dict(request, app_label)

        app_list = sorted(app_dict.values(), key=lambda x: x["name"].lower())

        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list

admin_site = MyAdminSite()
admin.site = admin_site


class ToursAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "location",
        "date",
        "price",
        "online",
        )

    fToursInfo = {"fields": (
        ("name","price","online"),
        ("location","date"),
        "banner",
        "description",
        )}

    
    fieldsets = (
        ("Informacion", fToursInfo),
        )

    list_filter = ["online"]
    search_fields = ['name']


class SettingsAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "IsActive",
        )

    fSettingsInfo = {"fields": (
        ("post1","post1_banner"),
        ("post2","post2_banner"),
        ("post3","post3_banner"),
        )}

    
    fieldsets = (
        ("", fSettingsInfo),
        )

    list_filter = ["IsActive"]

admin.site.register(model.Tours, ToursAdmin)
admin.site.register(model.Settings, SettingsAdmin)