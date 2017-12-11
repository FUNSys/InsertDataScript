import FunsysModel
#0:配属前 1:情シスICT ABCD 2:デザインEF 3:複雑GHIJ 4:知能KL 5:修士
kumi = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
def Invoke():
    id = 101
    classes = []
    while id < 602:
        for classid in kumi:
            schoolclass = FunsysModel.Class()
            schoolclass.class_id = id
            schoolclass.disp_class = str(id // 100) + classid
            if id // 100 == 1:
                schoolclass.course = 0
            elif id % 100 < 5:
                schoolclass.course = 1
            elif id % 100 < 7:
                schoolclass.course = 2
            elif id % 100 < 10:
                schoolclass.course = 3
            else:
                schoolclass.course = 4
            print(schoolclass)
            classes.append(schoolclass)
            id += 1
        id += 88
        if id > 500:
            schoolclass = FunsysModel.Class()
            schoolclass.class_id = id
            schoolclass.disp_class = "M1"
            schoolclass.course = 5
            print(schoolclass)
            classes.append(schoolclass)
            schoolclass = FunsysModel.Class()
            schoolclass.class_id = 601
            schoolclass.disp_class = "M2"
            schoolclass.course = 5
            print(schoolclass)
            classes.append(schoolclass)
            id = 1001
    #print()
    for schoolclass in classes:
        schoolclass.save(force_insert=True)
    FunsysModel.db.commit()

if __name__ == '__main__':
    Invoke()
