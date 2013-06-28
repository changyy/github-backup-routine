import json
import urllib2
import os

backup_path = "~/Dropbox/github"
username = "changyy"
github_api = "https://api.github.com/users/"+username+"/repos"

for page in range(1,10000):
	raw = urllib2.urlopen(github_api+"?page="+str(page)).read()
	parser = json.loads(raw)
	for repo in parser:
		print "Target:" + repo["clone_url"]
		os.system( "cd " + backup_path + " && (( test -e " + repo["name"] + " && cd " + repo["name"] + " && git pull ) ||  git clone " + repo["clone_url"] + " ) " )
	if len(parser) < 30:
		print "Total: "+str( 30*(page-1) + len(parser))
		break
