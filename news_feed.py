import requests

def view_feeds():
	return( requests.get('http://34.207.10.230:3000/posts').json())

def view_specific_feed(posts_id):
	"""post_id represents the index of specific data in the posts"""
    	data = requests.get('http://34.207.10.230:3000/posts').json()
    	return data[posts_id]
	

def post_feed():
	pass

def comment():
	pass

