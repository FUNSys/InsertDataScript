import FunsysModel
import json
import csv


def Invoke():
    lecturesinstances = []
    with open("data2/timetable.json") as f:
        json_data = json.load(f)
        lecturesinstances = [JsonToLectureClass(x) for x in json_data]
    FunsysModel.db.commit()


def JsonToLectureClass(x):
    lectureInstance = FunsysModel.Lecture()

    lectureInstance.disp_lecture = x["CourseName"]
    lectureInstance.week = x["WeekNumber"]
    lectureInstance.jigen = x["TimeNumber"]
    lectureInstance.save()
    classes = []
    if x["TargetClass"]:
        with open('data2/timetable_class_integration.csv', 'r') as f:
            reader = csv.reader(f)
            classes = [y[1:] for y in reader if y[0] == x["TargetClass"]][0]
    if classes:
        lectureInstance.classes = [FunsysModel.Class.get(
            FunsysModel.Class.class_id == y) for y in classes]
    lectureInstance.rooms = [FunsysModel.Room.get(
        FunsysModel.Room.disp_room == y) for y in x["Rooms"]]
    teachers = []
    if x["Teachers"]:
        for teacher in x["Teachers"]:
            with open('data2/timetable_teachers_integration.csv', 'r') as f:
                reader = csv.reader(f)
                for integration in reader:
                    if integration[0] == teacher:
                        teachers.append(integration[1])
                        break

    if teachers:
        lectureInstance.teachers = [FunsysModel.Teacher.get(
            FunsysModel.Teacher.disp_teacher == y) for y in teachers]
    lectureInstance.save()
    print(lectureInstance)

    return ""


if __name__ == '__main__':
    Invoke()
