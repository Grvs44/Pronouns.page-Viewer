import sys

class Profile:
    base_opinions = {
        'yes': 'Yes',
        'no': 'Nope',
        'meh': 'Okay',
        'jokingly': 'Jokingly',
        'close': 'Only if we\'re close',
    }

    def __init__(self, profile_data: dict, out_file=sys.stdout):
        self.data = profile_data
        self.opinions = dict(self.base_opinions)
        self.out_file = out_file
        for opinion in self.data.get('opinions', {}):
            self.opinions[opinion] = self.data['opinions'][opinion].get(
                'description')

    def _print_opinion_list(self, heading: str, items: list, indent: str = ''):
        print(indent + heading, file=self.out_file)
        for item in items:
            print(indent, item.get('value'), self.opinions.get(
                item.get('opinion')), sep='\t', file=self.out_file)

    def _print_list(self, heading: str, key: str):
        print(heading + ':', ', '.join(self.data.get(key, [])), file=self.out_file)

    def _print_words(self):
        print('Words', file=self.out_file)
        for category in self.data.get('words', []):
            self._print_opinion_list(category.get(
                'header'), category.get('values', []), '\t')

    def _print_custom_flags(self):
        flags = self.data.get('customFlags', [])
        if len(flags) == 0:
            return
        print('Custom flags', file=self.out_file)
        for flag in flags:
            if flag.get('description'):
                print(f"\t{flag['name']}\t{flag['description']}", file=self.out_file)
            else:
                print('\t' + flag['name'], file=self.out_file)

    def print(self):
        if 'description' in self.data:
            print(self.data['description'], file=self.out_file)
        if 'age' in self.data:
            print('Age:', self.data['age'], file=self.out_file)
        if 'links' in self.data:
            self._print_list('Links', 'links')
        if 'flags' in self.data:
            self._print_list('Flags', 'flags')
        if 'customFlags' in self.data:
            self._print_custom_flags()
        print(file=self.out_file)
        if 'names' in self.data:
            self._print_opinion_list('Names', self.data['names'])
        if 'pronouns' in self.data:
            self._print_opinion_list('Pronouns', self.data['pronouns'])
        if 'words' in self.data:
            self._print_words()


def print_page(page: dict, file=sys.stdout):
    print('Username:', page.get('username', '<no username>'), file=file)
    for profile in page.get('profiles', {}):
        print('Profile', profile, file=file)
        Profile(page['profiles'].get(profile, {}), file).print()
    if file is not sys.stdout:
        file.close()
