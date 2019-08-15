from django.conf.urls import url
from .import views
app_name='Rapp_APIView_p_id'
urlpatterns = [
    url(r'^$',views.input),
    url(r'^link$',views.link),
    url(r'^display$',views.display),
    url(r'^productapi$',views.ProductList.as_view()),
    url(r'^inputid$', views.inputid),
    url(r'^product$',views.ProductDetail.as_view()),
]