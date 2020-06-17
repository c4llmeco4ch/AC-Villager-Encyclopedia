import click
from db import db_setup, driver, Villager


@click.command()
@click.option('--name', '-n', help='The name of a villager you wish to find')
@click.option('--species', '-s',
              help='A species of villager to find', multiple=True)
@click.option('--personality', '-p',
              help='The personality you want to search for', multiple=True)
@click.option('--birth-month',
              help='Find villagers whose birthday is in the month')
@click.option('--birth-day',
              help='Find villagers whose birthday is on the day of the month')
def go():
    pass


if __name__ == '__main__':
    go()