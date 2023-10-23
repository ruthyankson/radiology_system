from django.contrib.auth.mixins import  LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.admin import AdminSite
from django.contrib.admin.sites import site
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from patients.models.ImageRequest import ImageRequest as modelHere
from patients.models.ImageRequestApproval import ImageRequestApproval
from patients.admin.mixins import ImageRequestApprovalMixin


class ImageRequestDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView, ImageRequestApprovalMixin):
    permission_required = "patients.view_image_request"
    template_name = "admin/patients/image_request_detail.html"
    model = modelHere
    context_object_name = 'image_request'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_request_pk = self.kwargs['pk']
        instance = modelHere.objects.get(pk=image_request_pk)
        admin_site: AdminSite = site
        context['title'] = 'Detail'
        context['patient'] = instance.patient
        context['labels'] = instance.fields_verbose
        context['patient_labels'] = instance.patient.fields_verbose 

        if (instance):            
            context['labels'] = instance.fields_verbose    

        request_approval = ImageRequestApproval.objects.get(image_request=image_request_pk)
        context['request_approval'] = request_approval
        # context['approval'] = request_approval.approval
        context['approval_labels'] = request_approval.fields_verbose


        context.update(self.get_form_image_request_approval_context(rk=image_request_pk))
        context.update(**admin_site.each_context(self.request))             
        return context

    def post(self, request, *args, **kwargs):
        image_request_pk = self.kwargs['pk']
        form_image_request_approval = self.get_form_image_request_approval(image_request_pk)
        if form_image_request_approval.is_valid():
            form_image_request_approval.save()
            # After saving, you can redirect to a success page, or maybe the same page.
            return HttpResponseRedirect(reverse("admin:image_request_detail", args=[image_request_pk]))
        # Handle the case where the form is not valid.
        # Re-render the detail page with the form and its errors.
        context = self.get_context_data(**kwargs)
        context['form_image_request_approval'] = form_image_request_approval
        # return context
        return render(request, self.template_name, context)

   