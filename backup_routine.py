import json
import urllib2
import os

backup_path = "~/Dropbox/github"
username = "changyy"
github_api = "https://api.github.com/users/"+username+"/repos"

raw = urllib2.urlopen(github_api).read()
parser = json.loads(raw)
for repo in parser:
	print "Target:" + repo["clone_url"]
	os.system( "cd " + backup_path + " && (( test -e " + repo["name"] + " && cd " + repo["name"] + " && git pull ) ||  git clone " + repo["clone_url"] + " ) " )
