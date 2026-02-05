from django.urls import path
from.views import *

urlpatterns=[
    path("create/", create_job),
    path("list/", list_jobs),
    path("update/<int:job_id>/", update_job),
    path("delete/<int:job_id>/", delete_job),
    path("apply/<int:job_id>/", apply_job),

    # UI Pages
    path("list/page/", job_list_page, name="job_list_page"),
    path("create/page/", create_job_page, name="create_job_page"),
    path("apply/page/", apply_job_page, name="apply_job_page"),
]