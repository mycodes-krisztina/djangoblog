from django.contrib import admin

# Register your models here.
from .models import Post  # .models a relatív import

class PostModelAdmin(admin.ModelAdmin):
    list_display=["title","updated","timestamp"]
    list_display_links=["updated"]
    list_filter =["updated","timestamp"]
    search_fields=["title"] #content -> a tartalomban is keres pl.
    list_editable=["title"] #items you can edit
    class Meta:
        model=Post

admin.site.register(Post, PostModelAdmin) #admin függvény,ami regisztrálja a Post modult az admin oldalra
#így kötődik össze a Post model és a PostModelAdmin