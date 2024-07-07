import requests


def fetchingAPI():
    apiData = requests.get(
        "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=sports&inc=categories%2Cid%2Ccontent&page=1")
    jsonData = apiData.json()

    if jsonData["statusCode"] == 200 and jsonData["success"]:
        jokes = jsonData['data']['data']

        for joke in jokes:
            print("=========================")
            print(joke['content'])
        print("=========================")
    else:
        raise Exception("Failed to fetch")


def main():
    try:
        fetchingAPI()
    except Exception:
        print('Failed to fetch')


if __name__ == "__main__":
    main()
