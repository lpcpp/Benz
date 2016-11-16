# -*- coding: utf-8 -*-
import index
import auth.urls
import admin.urls


urlpatterns = [
    (r"/?", index.IndexHandler),
    (r"/test/?", index.Test),
]


urlpatterns += auth.urls.urlpatterns + admin.urls.urlpatterns
