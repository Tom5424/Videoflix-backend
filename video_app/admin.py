from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Video, Genre


admin.site.register(Genre)


class VideoResource(resources.ModelResource):
    

    class Meta:
        model = Video


@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    exclude = ["video_image", "image_created", "video_progress"]
    resource_classes = [VideoResource]