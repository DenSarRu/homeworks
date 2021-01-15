def user_information(first_name, second_name, year_of_birthday, city_of_living, email, tel):
    print(f"Фамилия: {first_name}; Имя: {second_name}; год рождения: {year_of_birthday};'"
          f"город проживания: {city_of_living}; e-mail: {email}; номер телефона: {tel}")


data_entry = ['Фамилия', 'Имя', 'Год рождения', 'Город проживания', 'e-mail', 'Номер телефона']
entered_data = []
print('Введите данные о пользователе:')
for param in data_entry:
    entered_data.append(input(f'{param[:16]:>16}: '))

user_information(first_name=entered_data[0], second_name=entered_data[1], year_of_birthday=entered_data[2],
                 city_of_living=entered_data[3], email=entered_data[4], tel=entered_data[5])
