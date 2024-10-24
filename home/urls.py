from django.urls import path
from django.conf import settings
from home.views import *
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('permissions/', PermissionListView.as_view(), name='permissionList'),
    path('assign-permission/', AssignPermissionView.as_view(), name='assignPermission'),
    path('remove-permission/', RemovePermissionView.as_view(), name='removePermission'),
    path('permissions/<int:user_id>/', UserPermissionsView.as_view(), name='userPermissions'),

    path('users/', UserListView.as_view(), name='getUsers'),
    path('user/<int:user_id>/', UserDetailView.as_view(), name='userDetail'),

    path('departments/', DepartmentListCreateView.as_view(), name='getDepartmentListCreate'),
    path('department/<int:department_id>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='departmentRetrieveUpdateDestroy'),

    path('employees/', EmployeeListCreateView.as_view(), name='getEmployeeListCreate'),
    path('employee/<int:employee_id>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employeeRetrieveUpdateDestroy'),

    path('fields/', FieldListCreateView.as_view(), name='getFieldListCreate'),
    path('field/<int:field_id>/', FieldRetrieveUpdateDestroyView.as_view(), name='fieldRetrieveUpdateDestroy'),

    path('assignments/', AssignmentListCreateView.as_view(), name='getAssignmentListCreate'),
    path('assignment/<int:assignment_id>/', AssignmentRetrieveUpdateDestroyView.as_view(), name='assignmentRetrieveUpdateDestroy'),
    path('assignment/<int:assignment_id>/end/', EndAssignmentView.as_view(), name='EndAssignment'),

    path('attendances/', AttendanceListCreateView.as_view(), name='getAttendanceListCreate'),
    path('attendance/<int:attendance_id>/', AttendanceRetrieveUpdateDestroyView.as_view(), name='attendanceRetrieveUpdateDestroy'),
    
    # Mark attendance using tag_id
    path('mark-attendance/', MarkAttendanceView.as_view(), name='markAttendance'),
    
    # Get today's attendance
    path('today-attendance/', TodayAttendanceView.as_view(), name='todayAttendance'),
    
    # Get attendance by department
    path('department-attendance/<int:department_id>/', DepartmentAttendanceView.as_view(), name='departmentAttendance'),
    
    # Get employee attendance history
    path('employee-attendance/<int:employee_id>/', EmployeeAttendanceHistoryView.as_view(), name='employeeAttendanceHistory'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)