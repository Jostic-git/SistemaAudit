from django.contrib import admin

from hotline.models import HotLineItem, CategoryHotLine, SubCategoryHotLine, HotLineFile, HotLineComment

admin.site.register(HotLineItem)
admin.site.register(CategoryHotLine)
admin.site.register(SubCategoryHotLine)
admin.site.register(HotLineFile)
admin.site.register(HotLineComment)
