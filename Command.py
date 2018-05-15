import os  # os.sep
import os.path as osp
import shutil
import sys  # sys.exit
import traceback
import stat

import requests
from git import Repo

import Credentials
import Logging

#log = Logging.Log


class Command():

    params = None
    repos = []
    credentials = None
    github_api_url = None
    github_clone_url = None
    workspace = "./wip"
    cloned_repo = None
    repo_obj = Repo()
    new_branch = None

    def __init__(self, params):
        self.params = params
        self.credentials = Credentials.Credentials(params["credentials"])

    set

    def set_github_api_url(self):
        if "host_name" in self.params:
            host_name = self.params["host_name"]
            self.github_api_url = "https://" + host_name + "/api/v3"
        else:
            self.github_api_url = "https://api.github.com"
        print("API calls made to " + self.github_api_url)

    def set_github_clone_url(self, repo):
        self.github_clone_url = "https://"
        if "host_name" in self.params:
            self.github_clone_url = self.github_clone_url + \
                self.params["host_name"] + "/"
        else:
            self.github_clone_url = self.github_clone_url + "github.com/"

        if "org" in self.params:
            self.github_clone_url = self.github_clone_url + \
                self.params["org"] + "/"
        else:
            self.github_clone_url = self.github_clone_url + self.credentials.username + "/"

        self.github_clone_url = self.github_clone_url + repo + ".git"

    def get_repos(self):
        if "org" in self.params:
            self.get_org_repos(self.params["org"])
        else:
            self.get_user_repos()

    def get_org_repos(self, org):
        print("Feching repos from org:" + org)
        r = requests.get(self.github_api_url + "/orgs/" + org + "/repos",
                         auth=(self.credentials.username, self.credentials.password))
        if(r.status_code == 200):
            repos_json = r.json()

            for repo_json in repos_json:
                self.repos.append(repo_json["name"])

            print(self.repos)
        else:
            print(r.status_code)

    def get_user_repos(self):
        print("Feching repos from user:" + self.credentials.username)
        r = requests.get(self.github_api_url + "/users/" + self.credentials.username +
                         "/repos", auth=(self.credentials.username, self.credentials.password))

        if(r.status_code == 200):
            repos_json = r.json()

            for repo_json in repos_json:
                self.repos.append(repo_json["name"])

            print(self.repos)
        else:
            print(r.status_code)

    def clone(self, repo):
        print("Now cloning " + repo)
        os.mkdir(self.workspace)
        self.set_github_clone_url(repo)

        try:
            self.cloned_repo = self.repo_obj.clone_from(self.github_clone_url, self.workspace)
        except Exception as e:
            print(e)

    def find_and_replace(self, file_path, find, replace):
        # Read in the file
        with open(file_path, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(find, replace)

        # Write the file out again
        with open(file_path, 'w') as file:
            file.write(filedata)

    def create_new_branch(self):
        arr = self.params["file_path"].split("/")
        arr = arr[len(arr) - 1]
        file_name = arr.split(".")[0]
        print(file_name)
        
        self.new_branch = self.cloned_repo.create_head('droggo-' + file_name)
        print("New branch created: " + 'droggo-' + file_name)
        self.new_branch.checkout()
        
    def execute(self):
        self.set_github_api_url()
        self.get_repos()
        print(self.repos)
        for repo in self.repos:
            self.clone(repo)
            self.find_and_replace(self.workspace + "/" + self.params["file_path"], self.params["find"], self.params["replace"])
            self.create_new_branch()
            # self.stage()
            # self.commit()
            # self.raise_PR()
            shutil.rmtree(self.workspace, onerror=onerror)

def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """

    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise Exception


