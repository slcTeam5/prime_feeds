import requests

def url(path):
    return 'http://34.207.10.230:3000' + path


def view_feeds():
	pass

def post_feed():
	pass


def comment(comment_post='', p_id='', c_id=''):
    return requests.post('http://34.207.10.230:3000/comments', data=[{
        "body": comment_post,
        "postId": p_id,
        "id": c_id
    }])
