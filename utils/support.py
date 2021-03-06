from prettytable import PrettyTable


def user_input():
    """
    User input as long as the user input something
    :return:
    """
    while True:
        query = input('typ hier de naam van de film: ')

        if query:
            break

    return query


def print_table(movies):
    """
    Print movie information as table
    :param movies: array
    :return: table
    """
    table = PrettyTable(['Titel', 'aantal stemmen', 'gemiddelde score', 'datum', 'Populariteit', 'originele taal'])

    for movie in movies:
        table.add_row([movie['title'], movie['vote_count'], movie['vote_average'], movie['release_date'], movie['popularity'], movie['original_language']])

    return table
