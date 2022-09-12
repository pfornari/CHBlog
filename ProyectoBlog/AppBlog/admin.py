from django.contrib import admin

from AppBlog.models import Usuario, Categoria, Post, Tags, Comentarios

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Comentarios)
