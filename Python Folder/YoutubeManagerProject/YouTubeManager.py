import json


def videoSaver(videos):
    with open('ytVideos.py', 'w') as file:
        json.dump(videos, file)


def listVideos(videos):
    newVideos = enumerate(videos, start=1)

    print('\n============================')
    for i, v in newVideos:
        print(f'{i}.{v['name']} {v['time']}')

    print('============================')


def addVideo(videos):
    name = input("Enter Video name = ")
    time = input("Enter time = ")

    videos.append({'name': name, 'time': time})

    videoSaver(videos)


def updateVideo(videos):
    listVideos(videos)
    numInput = int(input('choose the video number = '))

    if 1 <= numInput <= len(videos):
        name = input("Enter new name = ")
        time = input("Enter new time = ")

    videos[numInput-1] = {'name': name, 'time': time}
    videoSaver(videos)


def deleteVideo(videos):
    listVideos(videos)

    num = int(input("Enter number of video to delete = "))

    if 1 <= num <= len(videos):
        del videos[num-1]

    videoSaver(videos)


def loadVideos():
    try:
        with open('ytVideos.py', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


choiceHolder = ''

while (True):
    videos = loadVideos()
    print("\nYoutube Manager Application")
    print('1.List all videos.')
    print('2.Add a Youtube video.')
    print('3.Update a Youtube video details.')
    print('4.Delete a youtube video.')
    print('5.Exit the application.')

    choiceHolder = input("Select any option : ")

    match choiceHolder:
        case '1':
            listVideos(videos)
        case '2':
            addVideo(videos)
        case '3':
            updateVideo(videos)
        case '4':
            deleteVideo(videos)
        case '5':
            break
        case _:
            print("INVALID ! Please choose a correct option")
