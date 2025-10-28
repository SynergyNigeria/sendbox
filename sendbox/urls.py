"""sendbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# import imp
from django.contrib import admin
from django.urls import path
from send_box_app import views as sv
from tracker.views import SearchClass, PackageDetailView
from django.conf.urls.static import static
from django.conf import settings

from sendbox.settings import MEDIA_ROOT

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", sv.index_view, name="index"),
    path("parcel_details", SearchClass.as_view(), name="parcel_details"),
    path("package/<str:order_id>/", PackageDetailView.as_view(), name="package_detail"),
    # path('parcel_details', sv.SearchClass.as_view(), name='parcel_details'),
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
