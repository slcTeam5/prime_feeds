import requests

def url(path):
    return 'http://34.207.10.230:3000' + path


def view_feed():
    resp = requests.get(url('/posts'))
    print(resp.content)


def post_news():
    title = input("Enter News Feed Title Between '': ")
    body = input("Enter News Feed Body Between '': ")
    return requests.post(url('/posts'), json={
        'title': title,
        'body': body
    })


def comment():
    postId = input("Enter News Feed Post Id Between '': ")
    body = input("Enter News Feed Comment Between '': ")
    return requests.post(url('/comments'), json={
        "body": body,
        "postId": postId
    })

def display_menu():
    print("")
    print("----------------------------------------")
    print("Welcome To The News Feed App ! :")
    print("")
    print("Select An Option")
    print("")
    print("1. View News Feeds")
    print("2. Post A News Feed")
    print("3. Comment On News Feed")
    print("")

