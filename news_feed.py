import requests

def view_feeds():
	
	return requests.get('http://34.207.10.230:3000/posts')

def view_specific_fee(posts_id):
	
	return requests.get('/http://34.207.10.230:3000/posts/{:id}' .format(posts_id))
	

def post_feed():
	pass

def comment():
	pass

