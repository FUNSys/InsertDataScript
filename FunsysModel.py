# -*- coding: utf-8 -*-
from peewee import *
from playhouse.fields import ManyToManyField
from playhouse.db_url import connect
import os

url = os.getenv(
    "FUNSYSDBURL", "mysql:///:memory:")

db = connect(url)


class JSONField(TextField):
    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)


class BaseModel(Model):
    class Meta:
        database = db


class Teacher(BaseModel):
    teacher_id = PrimaryKeyField()
    disp_teacher = TextField()
    roman_name = TextField(null=True)
    position = TextField(null=True)
    research_area = TextField(null=True)
    role = TextField(null=True)

    def __repr__(self):
        return '<Teacher_Model id={0}, disp={1}, roman={2}, potision={3}, area={4}, role={5}>'.format(
            self.teacher_id, self.disp_teacher, self.roman_name, self.position, self.research_area, self.role)


class Room(BaseModel):
    room_id = PrimaryKeyField()
    disp_room = TextField()

    def __repr__(self):
        return '<Room_Model id={0}, disp={1}>'.format(
            self.room_id, self.disp_room)


class Class(BaseModel):
    class_id = IntegerField(primary_key=True)
    disp_class = TextField()
    course = IntegerField()

    def __repr__(self):
        return '<Class_Model id={0}, disp_class={1}, course={2}>'.format(
            self.class_id, self.disp_class, self.course)


class Lecture(BaseModel):
    lecture_id = PrimaryKeyField()
    disp_lecture = TextField()
    must = JSONField(null=True)
    week = IntegerField()
    jigen = IntegerField()

    teachers = ManyToManyField(Teacher, related_name="lectures")
    rooms = ManyToManyField(Room, related_name="lectures")
    classes = ManyToManyField(Class, related_name="lectures")

    def __repr__(self):
        return '<Lecture_Model id={0}, disp={1}, must={2}, week={3}, jigen={4}, teacherscount={5}, roomscount={6}, classescount={7}>'.format(
            self.lecture_id, self.disp_lecture, self.must, self.week, self.jigen, len(
                self.teachers), len(self.rooms), len(self.classes))


LectureTeacher = Lecture.teachers.get_through_model()
LectureRoom = Lecture.rooms.get_through_model()
LectureClass = Lecture.classes.get_through_model()


def InitializeDatabase():
    db.drop_tables([Teacher, Room, Class, Lecture,
                    LectureTeacher, LectureRoom, LectureClass], safe=True)
    db.create_tables([Teacher, Room, Class, Lecture,
                      LectureTeacher, LectureRoom, LectureClass], safe=True)
    db.commit()


if __name__ == '__main__':
    InitializeDatabase()
