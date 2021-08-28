from django.conf.urls import include, url
from django.urls import path
from . import views


urlpatterns = [
    path("get_student_details",views.GetAllStudents.as_view()),
    path("insert_student_details", views.InsertStudentData.as_view()),
    path("update_student_details/<int:pk>",views.UpdateStudentData.as_view()),
    path("delete_student_details/<int:pk>",views.DeleteStudentData.as_view())
]


## ##################################################################################
## TESTING
## ##################################################################################

# http://127.0.0.1:8000/app_db_serializer/get_student_details
"""
Use the method = GET HTTP  in postman
"""

# http://127.0.0.1:8000/app_db_serializer/insert_student_details
"""
# With postman apply the following
1. Method = POST 
2. Content = Body>Raw
3. type = JSON

content
--------
{
    "student_id": 2
    ,"student_name":"B"
    ,"join_date":"2020-11-19"
}

"""

# http://127.0.0.1:8000/app_db_serializer/update_student_details/222
"""
# With postman apply the following
1. Method = PUT 
2. Content = Body>Raw
3. type = JSON

content
--------
{
    "student_id": 222
    ,"student_name":"AA"
    ,"join_date":"2020-11-19"
}

"""


# http://127.0.0.1:8000/app_db_serializer/delete_student_details/1
"""
# With postman apply the following
1. Method = DELETE 
No Content To Pass
"""


