import os  # os.sep
import sys  # sys.exit
import Credentials
import Logging

from github import Github


log = Logging.Log

class Command():

    params = None
    repos = []
    credentials = None
    org = None
    github = None

    def __init__(self, params):
        self.params = params
        self.credentials = Credentials.Credentials(params.credentials)

    def init_remote(self):
        try:
            self.github = Github(base_url="https://{self.credentials.username}/api/v3", login_or_token=self.credentials.password)
        except Exception as e:
            print(e)
            log.info("Log in as enterprise failed. Now trying log in as personal github")
            try:
                self.github = Github(self.credentials.username, self.credentials.password)
            except Exception as e:
                print(e)
                log.err("Login failed")
                sys.exit(1)

        try:
            self.org = self.github.get_organization(params.org)
        except Exception as e:
            log.err(e)

    def get_repos(self):
        try:
            self.repos = self.org.get_repos()
        except Exception as e:
            print(e)

    def execute(self):
        self.init_remote()
        self.get_repos()
        for repo in self.repos:
            # self.clone()
            # self.find_and_replace()  
            pass  
        
        