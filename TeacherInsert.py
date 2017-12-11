import FunsysModel
import csv

# position,name,roman,rorle,research,


def Invoke():
    teachers_csv = []
    with open('data2/teachers_main.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        teachers_csv = [x for x in reader]
    timetable_teachers_integration = []
    with open('data2/timetable_teachers_integration.csv') as f:
        reader = csv.reader(f)
        timetable_teachers_integration = [x for x in reader]
    
    for teacher in timetable_teachers_integration:
        if [x for x in teachers_csv if x[1] == teacher[1]]:
            teacherinfo = [x for x in teachers_csv if x[1] == teacher[1]][0]
            teacher_model = FunsysModel.Teacher()
            teacher_model.position = teacherinfo[0]
            teacher_model.disp_teacher = teacherinfo[1]
            teacher_model.roman_name = teacherinfo[2]
            teacher_model.role = teacherinfo[3]
            teacher_model.research_area = ",".join(teacherinfo[4:])

            teacher_model.save()
            print(teacher_model)
        else:
            teacher_model = FunsysModel.Teacher()
            teacher_model.disp_teacher = teacher[1]
            teacher_model.save()
            print(teacher_model)
    FunsysModel.db.commit()


if __name__ == '__main__':
    Invoke()
