from app.views import baseView
from app.views import user
app_name = 'APP'
urlpatterns = [
    ("/logout",user.UserLogOut),
    ("/login",user.UserView),
    ("/test",baseView.ThingsResource),
    ("/root",'app.urls.urlpatterns')
]
