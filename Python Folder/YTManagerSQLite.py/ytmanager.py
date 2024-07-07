import sqlite3
con = sqlite3.connect("manager.db")

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS YtManager(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL    
    )''')


def listVideos():
    fields = cur.execute('SELECT * FROM YtManager')

    print("\n******************************")
    for i in fields:
        print(i)
    print("******************************")


def addVideo(name, time):
    cur.execute("INSERT INTO YtManager (name,time) VALUES (?,?)", (name, time))
    con.commit()


def updateVideo(id, name, time):
    cur.execute("UPDATE YtManager SET name=?, time=? WHERE id=?",
                (name, time, id))
    con.commit()


def deleteVideo(id):
    cur.execute("DELETE FROM YtManager WHERE id=?", (id,))
    print("***Deleted successfully***")
    con.commit()


def main():
    while (True):
        print("\nYoutube Manager Application")
        print('1.List all videos.')
        print('2.Add a Youtube video.')
        print('3.Update a Youtube video details.')
        print('4.Delete a youtube video.')
        print('5.Exit the application.')

        choiceHolder = input("Select any option : ")

        if choiceHolder == '1':
            listVideos()
        elif choiceHolder == '2':
            name = input("\nEnter video name = ")
            time = input("Enter time= ")
            addVideo(name, time)
        elif choiceHolder == '3':
            listVideos()
            id = int(input("Enter id to update = "))
            name = input("Enter new name = ")
            time = input("Enter new time = ")
            updateVideo(id, name, time)
        elif choiceHolder == '4':
            listVideos()
            id = int(input("Enter id to delete = "))
            deleteVideo(id)
        elif choiceHolder == '5':
            break
        else:
            print("\n******************************")
            print("INVALID ! Please choose a correct option")
            print("********************************")


if __name__ == "__main__":
    main()
