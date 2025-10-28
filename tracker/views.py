from django.views.generic import ListView, DetailView
from .models import User_Package_Detail, TrackingTimeline
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.


class SearchClass(ListView):
    model = User_Package_Detail
    template_name = "dashboard.html"

    # defining quaryset
    def get_queryset(self):
        query = self.request.GET.get("track_id")
        object_list = User_Package_Detail.objects.filter(Q(order_id__iexact=query))

        return object_list

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("track_id")
        if query:
            # Try to find the package directly
            try:
                package = User_Package_Detail.objects.get(order_id__iexact=query)
                # Redirect to package detail page
                return redirect(
                    reverse("package_detail", kwargs={"order_id": package.order_id})
                )
            except User_Package_Detail.DoesNotExist:
                # If package not found, show dashboard with no results
                pass
        return super().get(request, *args, **kwargs)


class PackageDetailView(DetailView):
    model = User_Package_Detail
    template_name = "package_detail.html"
    context_object_name = "package"
    slug_field = "order_id"
    slug_url_kwarg = "order_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        package = self.get_object()
        # Add timeline entries to context
        context["timeline_entries"] = package.timeline_entries.all()
        return context
