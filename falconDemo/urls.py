from app.views import baseView
app_name = 'APP'
urlpatterns = [
    ("/test",baseView.ThingsResource),
    ("/root",'app.urls.urlpatterns')
]
