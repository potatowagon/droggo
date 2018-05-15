import os  # os.sep
import sys  # sys.exit
import traceback
import requests

import Credentials
import Logging




#log = Logging.Log

class Command():

    params = None
    repos = []
    credentials = None
    github_url = None

    def __init__(self, params):
        print("here")
        self.params = params
        self.credentials = Credentials.Credentials(params["credentials"])

    def set_github_url(self):
        if "host_name" in self.params:
            host_name = self.params["host_name"]
            self.github_url = "https://" + host_name + "/api/v3"
        else:
            self.github_url = "https://api.github.com"
        print("API calls made to " + self.github_url)

    def get_repos(self):
        self.set_github_url()
        if "org" in self.params:
            self.repos = self.get_org_repos(self.params["org"])
        else:    
            self.repos = self.get_user_repos()

    def execute(self):
        self.get_repos()
        #for repo in self.repos:
            # self.clone()
            # self.find_and_replace()
            # self.PR()  
            #print(repo.name)
           # pass
        
    def get_org_repos(self, org):
        print("Feching repos from org:" + org)
        r = requests.get(self.github_url + "/orgs/" + org + "/repos", auth=(self.credentials.username, self.credentials.password))
        if(r.status_code == 200):
            repos_json = r.json()
            
            for repo_json in repos_json:
                self.repos.append(repo_json["name"])
        
            print(self.repos)
        else:
            print(r.status_code)

    def get_user_repos(self):
        print("Feching repos from user:" + self.credentials.username)
        r = requests.get(self.github_url + "/user/repos", auth=(self.credentials.username, self.credentials.password))
        
        if(r.status_code == 200):
            repos_json = r.json()
            
            for repo_json in repos_json:
                self.repos.append(repo_json["name"])
            
            print(self.repos)
        else:
            print(r.status_code)   