import requests
from tabulate import tabulate
from os import system


class Pokemon:

    offset = 0
    limit = 100
    total_data = 10
    url = "https://pokeapi.co/api/v2/ability/?offset=" + \
        str(offset) + "&limit=" + str(limit)
    data = []

    def getPokemonData(self, order="ASC", page=1):
        header = ['No', 'Nama Pokemon', 'URL']
        response = requests.get(self.url).json()['results']
        self.data = []
        for i in range(len(response)):
            self.data.append([i+1, response[i]['name'], response[i]['url']])
        start = self.total_data * (page - 1)
        self.data = self.data[start:start+self.total_data]
        self.data = sorted(
            self.data, reverse=True if order == "DESC" else False)
        print(tabulate(self.data, header, tablefmt="github"))

    def preview(self):
        system('cls')
        print("="*16)
        print("DATA POKEMON")
        print("="*16)
        print()
        order = input("Urutan Data ASC/DESC : ").upper()
        page = int(input("Halaman : "))
        self.getPokemonData(order, page)
        again = input("Lihat Data Lainnya (Y/N) : ").upper()
        if again == "Y":
            self.preview()


Pokemon().preview()
