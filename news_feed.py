import requests

def view_feeds():
	print( requests.get('http://34.207.10.230:3000/posts').json())


	

def post_feed():
	pass

def comment():
	pass

