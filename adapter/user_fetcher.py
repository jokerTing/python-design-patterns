import csv

class UserFetcher(object):
    def __init__(self, source):
        self.source = source
    
    def fetch_users(self):
        with open(self.source, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            users = [row for row in reader]
            return users