#Simple bot that creates 30 strawpoll links
import requests, json, yaml

a = 0
while a < 30:
	url = "https://strawpoll.me/api/v2/polls"
	data = {'title': 'Should this video be added?', 'options': [ "Yes", "No"]}
	headers = {'Content-type': 'application/json'}
	r = requests.post(url, data=json.dumps(data), headers=headers)
	strawpoll_data =  yaml.load(r.text)
	id = strawpoll_data["id"]
	id = str(id)
	strawpoll = open('strawpolls.txt','a')
	strawpoll.write("http://strawpoll.me/"+id+"\n")
	a += 1
print "Done!"