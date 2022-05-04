import csv
import datetime
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
    header = ['chestie_id']
    data = []

    for i in range(no_entries_per_country):
        entry = [fd_id]
        data.append(entry)

        fd_id += 1

    write_to_csv('chestie.csv', header, data)


def generate_countries_data():
    countries = ['Romania', 'Germany', 'USA', 'Japan', 'Brazil']
    e_id = 1
    header = ['country_id', 'country']
    data = []

    for i in range(no_of_countries):
        entry = [e_id, countries[i]]
        data.append(entry)

        e_id += 1

    write_to_csv('countries.csv', header, data)


def generate_food_drinks_data(start_id):
    e_id = start_id
    header = ['fd_id', 'did_eat_meat', 'was_vegan', 'no_meals', 'no_snacks', 'alcohol_consumed', 'water_drank']
    data = []

    for i in range(no_entries_per_country*no_of_countries):
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
    header = ['social_id', 'family_time', 'work_time', 'friends_time', 'productive_time', 'relaxing_time']
    data = []

    for i in range(no_entries_per_country*no_of_countries):
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
    header = ['sleep_id', 'sleep_time', 'no_naps']
    data = []

    for i in range(no_entries_per_country*no_of_countries):

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
    header = ['spendings_id', 'food_drinks', 'clothes', 'entertainment', 'others']
    data = []

    for i in range(no_entries_per_country*no_of_countries):
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


def generate_happiness_data(start_id):
    header = ['happy_id', 'current_date', 'happy_score', 'country_id', 'fd_id', 'social_id', 'sleep_id', 'spendings_id']
    fd_id = 1
    data = []
    start_date = datetime.datetime.strptime('21/01/01', "%y/%m/%d")

    current_date = start_date
    for day in range(365):
        for i in range(no_entries_per_country*no_of_countries):
            for c in range(no_of_countries):
                happy_score = random.randint(1, 100)
                p = random.randint(1, 100)
                if p > 75:
                    happy_score += random.randint(0, min(50, 100 - happy_score))
                entry = [fd_id, current_date.date(), happy_score, c + 1, start_id, start_id, start_id, start_id]
                data.append(entry)

                fd_id += 1
                start_id += 1
        current_date = current_date + datetime.timedelta(days=1)
        start_id = start_id//1000*1000 + 1000

    write_to_csv('happiness.csv', header, data)


if __name__ == '__main__':
    # init_csv('countries.csv',  ['country_id', 'country'])
    # generate_countries_data()
    # init_csv('food_drinks.csv',  ['fd_id', 'did_eat_meat', 'was_vegan', 'no_meals', 'no_snacks', 'alcohol_consumed', 'water_drank'])
    # init_csv('social.csv',  ['social_id', 'family_time', 'work_time', 'friends_time', 'productive_time', 'relaxing_time'])
    # init_csv('sleep.csv',  ['sleep_id', 'sleep_time', 'no_naps'])
    # init_csv('spendings.csv',  ['spendings_id', 'food_drinks', 'clothes', 'entertainment', 'others'])
    start_id = 5000
    # for _ in range(365):
    #     generate_food_drinks_data(start_id)
    #     generate_social_data(start_id)
    #     generate_sleep_data(start_id)
    #     generate_spendings_data(start_id)
    #     start_id += 1000

    init_csv('happiness.csv',
             ['happy_id', 'current_date', 'happy_score', 'country_id', 'fd_id', 'social_id', 'sleep_id', 'spendings_id'])
    generate_happiness_data(start_id)
