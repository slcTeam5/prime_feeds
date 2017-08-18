import requests


def _url(path):
    return 'http://34.207.10.230:3000' + path

def get_posts(id=None):
    return requests.get(_url('/posts/'))

def get_post_by_id(id):
    return requests.get(_url('/posts/'+ str(id)))
"""
def describe_task(task_id):
    return requestsget(_url('/tasks/{:d}/'.format(task_id)))

def add_task(summary, description=""):
    return requests.post(_url('/tasks/'), json={
            'summary': summary,
            'description': description,
            })

def task_done(task_id):
    return requests.delete(_url('/tasks/{:d}/'.format(task_id)))

def update_task(task_id, summary, description):
    url = _url('/tasks/{:d}/'.format(task_id))
    return requests.put(url, json={
            'summary': summary,
            'description': description,
            }).
"""
def update_post(title, body, author, id):
    update ={"title": title, "body": body,
             "author": author, "id": id}
    response = requests.put(_url('/posts/'+id), json=update)
    return response.status_code

def get_posts_data():
    values = get_posts()
    return values.json()

def get_one_post(id):
    value = get_post_by_id(id)
    return value.json()

def create_post(title, body, author, id):
    post = {"title": title, "body": body,
            "author": author, "id": id}
    talk = requests.post(_url('/posts/'), json=post)

#print get_posts_data()

#create_post("team 5 again", "and again", "phil", "82")
update_post("team 5 again", "and again and again", "phil", "82")
print get_one_post(82)


