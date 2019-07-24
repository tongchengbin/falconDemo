from .views import baseView
app_name = 'API'
urlpatterns = [
    ('/test',baseView.ThingsResource)
]
