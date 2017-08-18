import requests


def _url(path):
    return 'http://34.207.10.230:3000' + path

def get_posts(id=None):
    return requests.get(_url('/posts/'))

def get_post_by_id(id):
    return requests.get(_url('/posts/'+ str(id)))

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

def delete_post(id):
    response = requests.delete(_url('/posts/'+str(id)))
    return response.status_code


#print get_posts_data()

#create_post("team 5 again", "and again", "phil", "82")
#update_post("team 5 again", "and again and again", "phil", "82")
#print get_posts_data()
print "====get one==="
print get_one_post(82)
print "===delete==="
print delete_post(82)
print "====get one===="
print get_one_post(82)
create_post("team 5 again", "and again", "phil", "82")
update_post("team 5 again", "and again and again", "phil", "82")
print get_one_post(82)



