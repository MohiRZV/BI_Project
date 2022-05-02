import csv
import random

no_entries_per_country = 10
no_of_countries = 5


def init_csv(file, header):
    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)


def write_to_csv(file, header, data):
    with open(file, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the data
        for entry in data:
            writer.writerow(entry)


def generate_chestie_data(start_id):
    fd_id = start_id
    header = ['fd_id']
    data = []

    for i in range(no_entries_per_country):
        entry = [fd_id]
        data.append(entry)

        fd_id += 1

    write_to_csv('chestie.csv', header, data)


def generate_countries_data():
    countries = ['Romania', 'Germany', 'USA', 'Japan', 'Brazil']
    e_id = 1
    header = ['c_id', 'country']
    data = []

    for i in range(no_entries_per_country):
        entry = [e_id, countries[i]]
        data.append(entry)

        e_id += 1

    write_to_csv('countries.csv', header, data)


def generate_food_drinks_data(start_id):
    e_id = start_id
    header = ['fd_id', 'did_eat_meat', 'was_vegan', 'no_meals', 'no_snacks', 'alcohol_consumed', 'water_drank']
    data = []

    for i in range(no_entries_per_country):
        did_eat_meat = bool(random.randint(0, 1))
        was_vegan = not did_eat_meat
        p = random.randint(0, 100)
        if was_vegan and p < 80:
            was_vegan = not was_vegan

        no_meals = random.randint(1, 3)
        p = random.randint(0, 100)
        if no_meals == 3 and p < 20:
            no_meals += random.randint(1, 4)

        no_snacks = random.randint(0, 5)
        alcohol_cosumed = 0
        p = random.randint(0, 100)
        if p > 75:
            alcohol_cosumed = random.randint(0, 1000)

        water_drank = random.randint(0, 2000) + 500
        p = random.randint(0, 100)
        if p > 83:
            water_drank += random.randint(0, 1000)

        entry = [e_id, did_eat_meat, was_vegan, no_meals, no_snacks, alcohol_cosumed, water_drank]
        data.append(entry)

        e_id += 1

    write_to_csv('food_drinks.csv', header, data)


def generate_social_data(start_id):
    e_id = start_id
    header = ['fd_id', 'family_time', 'work_time', 'friends_time', 'productive_time', 'relaxing_time']
    data = []

    for i in range(no_entries_per_country):
        time_available = 14

        p = random.randint(0, 100)
        family_time = 0
        if p > 80:
            family_time = random.randint(0, 4)
            time_available -= family_time

        p = random.randint(0, 70)
        if p > 50:
            work_time = random.randint(6, 10)
        else:
            work_time = 0
        time_available -= work_time

        friends_time = random.randint(0, min(2, time_available))
        time_available -= friends_time

        productive_time = random.randint(0, min(4, time_available))
        time_available -= productive_time

        relaxing_time = random.randint(0, min(4, time_available))
        time_available -= relaxing_time

        entry = [e_id, family_time, work_time, friends_time, productive_time, relaxing_time]
        data.append(entry)

        e_id += 1

    write_to_csv('social.csv', header, data)


def generate_sleep_data(start_id):
    e_id = start_id
    header = ['fd_id', 'sleep_time', 'no_naps']
    data = []

    for i in range(no_entries_per_country):

        no_naps = 0
        p = random.randint(0, 100)
        if p < 25:
            no_naps = random.randint(0, 5)

        sleep_time = random.randint(0, 10)

        entry = [e_id, sleep_time, no_naps]
        data.append(entry)

        e_id += 1

    write_to_csv('sleep.csv', header, data)


def generate_spendings_data(start_id):
    e_id = start_id
    header = ['fd_id', 'food_drinks', 'clothes', 'entertainment', 'others']
    data = []

    for i in range(no_entries_per_country):
        p = random.randint(0, 100)
        food_drinks = 0
        if p < 60:
            food_drinks = random.randint(0, 500)
        if p < 3:
            food_drinks += random.randint(100, 5000)

        p = random.randint(0, 100)
        clothes = 0
        if p < 35:
            clothes = random.randint(0, 500)
        if p < 3:
            clothes += random.randint(0, 5000)

        p = random.randint(0, 100)
        entertainment = 0
        if p < 45:
            entertainment = random.randint(0, 500)
        if p < 5:
            entertainment += random.randint(0, 5000)

        p = random.randint(0, 100)
        others = 0
        if p < 75:
            others = random.randint(0, 300)
        if p < 10:
            others += random.randint(0, 1000)

        entry = [e_id, food_drinks, clothes, entertainment, others]
        data.append(entry)

        e_id += 1

    write_to_csv('spendings.csv', header, data)


if __name__ == '__main__':
    init_csv('countries.csv',  ['c_id', 'country'])
    init_csv('food_drinks.csv',  ['fd_id', 'did_eat_meat', 'was_vegan', 'no_meals', 'no_snacks', 'alcohol_consumed', 'water_drank'])
    init_csv('social.csv',  ['fd_id', 'family_time', 'work_time', 'friends_time', 'productive_time', 'relaxing_time'])
    init_csv('sleep.csv',  ['fd_id', 'sleep_time', 'no_naps'])
    init_csv('spendings.csv',  ['fd_id', 'food_drinks', 'clothes', 'entertainment', 'others'])
    start_id = 5000
    for _ in range(365):
        generate_food_drinks_data(start_id)
        generate_social_data(start_id)
        generate_sleep_data(start_id)
        generate_spendings_data(start_id)
        start_id += 1000
