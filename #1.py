import requests


class SuperHero:

    def get_superheroes_list(self):
        files_url = 'https://akabab.github.io/superhero-api/api/all.json'
        response = requests.get(files_url, headers={'User-agent': 'someone'})
        return response.json()

    def find_superheroes_intelligence(self, heroes_list_compare):
        superheroes_list = self.get_superheroes_list()
        superheroes_intelligence_list = []
        superhero_intelligence = []
        for superhero in superheroes_list:
            for item in heroes_list_compare:
                if superhero['name'] == item:
                    superhero_intelligence.append(superhero['name'])
                    superhero_intelligence.append(superhero['powerstats']['intelligence'])
                    superheroes_intelligence_list.append(superhero_intelligence)
                    superhero_intelligence = []
        return superheroes_intelligence_list

    def the_most_intelligent_superhero(self, heroes_list_compare):
        superheroes_intelligence_list = self.find_superheroes_intelligence(heroes_list_compare)
        for i in range(len(superheroes_intelligence_list)):
            minimum = i
            for j in range(i + 1, len(superheroes_intelligence_list)):
                if superheroes_intelligence_list[j][1] < superheroes_intelligence_list[minimum][1]:
                    minimum = j
            superheroes_intelligence_list[minimum], superheroes_intelligence_list[i] = superheroes_intelligence_list[i], superheroes_intelligence_list[minimum]
        return f'The most intelligent superhero is {superheroes_intelligence_list[-1][0]}!'


if __name__ == '__main__':
    hulk = SuperHero()
    heroes_list_compare = ['Hulk', 'Captain America', 'Thanos', 'Spider-Man', 'Black Mamba', 'Ben 10']
    print(hulk.find_superheroes_intelligence(heroes_list_compare))
    print(hulk.the_most_intelligent_superhero(heroes_list_compare))
