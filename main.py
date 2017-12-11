import FunsysModel
import ClassInsert
import RoomInsert
import TeacherInsert
import LecturesInsert

if __name__ == '__main__':
    FunsysModel.InitializeDatabase()
    ClassInsert.Invoke()
    RoomInsert.Invoke()
    TeacherInsert.Invoke()
    LecturesInsert.Invoke()
    print("Initialize Complete")
    FunsysModel.db.commit()
    
