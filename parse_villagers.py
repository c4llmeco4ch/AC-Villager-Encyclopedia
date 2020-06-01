import requests
import re
from bs4 import BeautifulSoup, ResultSet
from typing import List, Tuple

WIKI_URL = 'https://animalcrossing.fandom.com/wiki/Villager_list_(New_Horizons)'
VILLAGER_PERSONALITIES = ['Cranky', 'Jock', 'Lazy', 'Smug', 'Normal', 'Peppy', 'Snooty', 'Sisterly']
VILLAGER_SPECIES = ['Alligator', 'Anteater', 'Bear', 'Bird', 'Bull',
    'Cat', 'Chicken', 'Cow', 'Cub', 'Deer',
    'Dog', 'Duck', 'Eagle', 'Elephant', 'Frog',
    'Goat', 'Gorilla', 'Hamster', 'Hippo', 'Horse',
    'Kangaroo', 'Koala', 'Lion', 'Monkey', 'Mouse',
    'Octopus', 'Ostrich', 'Penguin', 'Pig', 'Rabbit',
    'Rhino', 'Sheep', 'Squirrel', 'Tiger', 'Wolf']


def parse_row(r: ResultSet) -> Tuple[str, List[str]]:
    """Break up a villager's table row into the individual parts

    Arguments:
        r {ResultSet} -- The row to be parsed

    Returns:
        Tuple[str, List[str]] -- A villager's name and their attributes
    """
    bad_vals = re.compile(r'\W')
    cols = [re.sub(bad_vals, '', val.text) for val in r.find_all('td')]
    return (cols[0], cols[2:])


def find_villager_list() -> Dict[List[str]]:
    """Scrape a list of villagers from the Wiki, creating a list of villager info

    Returns:
        List[List[str]] -- The list of villagers with their respective information
    """
    villagers = {}
    page = BeautifulSoup(requests.get(WIKI_URL).content, 'lxml')
    #Pull the villager table from the page
    table = page.find(lambda tag: tag.name == 'table' and tag.has_attr('style') and 'background-color:#2C852C;' in tag['style'])
    rows = table.find_all('tr')[1:]
    for r in rows:
        name, attr = parse_row(r)
        villagers[name] = attr
    return villagers

        
        

if __name__ == '__main__':
    all_v = find_villager_list()
    specific = input("Which villager do you want to learn about: ")
    attrs = all_v[specific]
    print('\n'.join([f'{specific}\'s attributes:',
            f'Personality: {attrs[0]}',
            f'Species: {attrs[1]}',
            f'Birthday: {attrs[2]}',
            f'Catchphrase: {attrs[3]}',
            f'Hobbies: {attrs[4]}']))