from django.urls import path
from django.views.generic import TemplateView

app_name = 'pages'

urlpatterns = [
    path(
        'team/',
        TemplateView.as_view(template_name='pages/team.html'),
        name='team'
    ),
    path(
        'community/',
        TemplateView.as_view(template_name='pages/community.html'),
        name='community'
    ),
    path(
        'about/',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'
    ),
    path(
        'rules/',
        TemplateView.as_view(template_name='pages/rules.html'),
        name='rules'
    ),
]

 