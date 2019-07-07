from django.urls import path,include

from rest_framework import routers

from .views import StudentViewSet

from .views import TeacherViewSet

from .views import CourseViewSet

router = routers.DefaultRouter()
router.register("students",StudentViewSet)
router.register("teachers",TeacherViewSet)
router.register("Courses",CourseViewSet)

urlpatterns = [
	path("", include(router.urls)),
	path("", include(router.urls)),
	path("", include(router.urls)),
]


