
from django.contrib import admin
from index.models import Student, Teacher

# admin后台管理数据

admin.site.site_header = "学生成绩信息管理系统"
admin.site.site_title = "数据管理平台"
admin.site.index_title = "学生成绩管理"

# admin.site.register(Student)
# admin.site.register(Teacher)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_bottom = False
    actions_on_top = True
    list_display = ['stu_id', 'stu_name', 'sex', 'chinese', 'mathematics', 'English']
    search_fields = ['stu_id']     # 搜索，按照id

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_bottom = False
    actions_on_top = True
    list_display = ['tea_id', 'name', 'age']
    search_fields = ['tea_id']     # 搜索，按照id
