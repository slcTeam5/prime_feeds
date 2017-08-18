import requests

def view_feeds():
	print( requests.get(_url('/posts')).json())


	

def post_feed():
	pass

def comment():
	pass

