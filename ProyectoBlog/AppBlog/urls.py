from django.urls import path

from AppBlog.views import * 
#usuario, tags, categoria, post, comentarios

urlpatterns = [
    path('', inicio, name='AppBlogInicio'),
    path('usuario/', usuario, name='AppBlogUsuario'),
    path('tags/', tags, name='AppBlogTags'),
    path('categoria/', categoria, name='AppBlogCategoria'),
    path('post/', post, name='AppBlogPost'),
    path('comentarios/', comentarios, name='AppBlogComentarios'),
    path('usuario_formulario/', usuario_formulario, name='AppBlogUsuarioFormulario'),
    path('categoria_formulario/', categoria_formulario, name='AppBlogCategoriaFormulario'),
    path('tag_formulario/', tag_formulario, name='AppBlogTagFormulario'),
    path('busqueda_usuario/', busqueda_usuario, name='AppBlogBusquedaUsuario'),
    path('busqueda_usuario_post/', busqueda_usuario_post, name='AppBlogBusquedaUsuarioPost'),
]
