import pymongo
from bson import ObjectId

client = pymongo.MongoClient(
    "mongodb+srv://shamin7860official:shamin7860@cluster0.xxwzf2v.mongodb.net/")

db = client['YTmanager']
collection = db['videos']

# print(collection)


def listVideos():
    print("\n******************************")

    for video in collection.find():
        print(f'ID:{video['_id']}, name:{video['name']}, time:{video['time']}')

    print("******************************")


def addVideo(name, time):
    collection.insert_one({'name': name, 'time': time})


def updateVideo(id, name, time):
    collection.update_one(
        {'_id': ObjectId(id)},
        {"$set": {'name': name, 'time': time}}
    )


def deleteVideo(id):
    collection.delete_one({'_id': ObjectId(id)})


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
            id = input("Enter id to update = ")
            name = input("Enter new name = ")
            time = input("Enter new time = ")
            updateVideo(id, name, time)
        elif choiceHolder == '4':
            listVideos()
            id = input("Enter id to delete = ")
            deleteVideo(id)
        elif choiceHolder == '5':
            break
        else:
            print("\n******************************")
            print("INVALID ! Please choose a correct option")
            print("********************************")


if __name__ == '__main__':
    main()
