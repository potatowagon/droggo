import os  # os.sep
import sys  # sys.exit
import traceback

import Credentials
import Logging

from github import Github


#log = Logging.Log

class Command():

    params = None
    repos = []
    credentials = None
    org = None
    github = None

    def __init__(self, params):
        print("here")
        self.params = params
        self.credentials = Credentials.Credentials(params["credentials"])

    def init_remote(self):
        try:
            print(self.credentials.username, self.credentials.password)
            self.github = Github(base_url="https://{self.credentials.username}/api/v3", login_or_token=self.credentials.password)
            print(self.github)
        except Exception as e:
            print(e)
            print("Log in as enterprise failed. Now trying log in as personal github")
            #log.info("Log in as enterprise failed. Now trying log in as personal github")
            try:
                self.github = Github(self.credentials.username, self.credentials.password)
            except Exception as e:
                print(e)
                print("Login failed")
                #log.err("Login failed")
                sys.exit(1)

        try:
            pass
        except Exception as e:
            print(e)
            

    def get_repos(self):
        try:
            #self.repos = self.org.get_repos()
            self.repos = self.github.get_repos()
        except Exception as e:
            print(e)

    def execute(self):
        self.init_remote()
        self.get_repos()
        for repo in self.repos:
            # self.clone()
            # self.find_and_replace()
            # self.PR()  
            print(repo.name)
        
        