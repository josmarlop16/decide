from django.contrib import admin

from .models import Census


class CensusAdmin(admin.ModelAdmin):
    list_display = ('voting_id', 'voter_id', 'adscrited_id', )
    list_filter = ('voting_id', 'adscrited_id', )

    search_fields = ('voter_id', )


admin.site.register(Census, CensusAdmin)
