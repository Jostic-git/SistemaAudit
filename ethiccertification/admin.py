from django.contrib import admin

from ethiccertification.models import EthicItem, EthicItemAnswer3, EthicItemAnswer4, EthicItemAnswer5, EthicItemAnswer2

admin.site.register(EthicItem)
admin.site.register(EthicItemAnswer2)
admin.site.register(EthicItemAnswer3)
admin.site.register(EthicItemAnswer4)
admin.site.register(EthicItemAnswer5)
