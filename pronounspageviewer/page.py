from . import Profile


class Page:
    def __init__(self, page_data: dict):
        self.data = page_data

    def print(self):
        print('Username:', self.data.get('username', '<no username>'))
        for profile in self.data.get('profiles', {}):
            print('Profile', profile)
            Profile(self.data['profiles'].get(profile, {})).print()
