import FunsysModel

def Invoke():
    with open('data2/rooms.csv', 'r') as f:
        name = f.readline()
        while name:
            name = name.replace('\n', '').replace('\"', '')
            room = FunsysModel.Room()
            room.disp_room = name
            room.save()
            print(room)
            name = f.readline()

    FunsysModel.db.commit()

if __name__ == '__main__':
    Invoke()
