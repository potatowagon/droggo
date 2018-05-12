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
        except:
            log