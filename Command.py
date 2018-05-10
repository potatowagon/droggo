import Credentials

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
        ##github