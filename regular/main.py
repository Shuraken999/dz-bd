import re
import csv
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
def search(text,pattern):    
    while True:
    	result = pattern.search(text)
    	if result != None:
    		print(result.groupdict())
    		text = text[result.end():]
    	else:
    		break
with open('phonebook_raw.csv') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
print('Было')
pprint(contacts_list)
#Создание патерна поиска и замены
pattern = r"([А-ЯЁ]{1}[а-яё]+)\W([А-ЯЁ]{1}[а-яё]+)(\W(?P<s>[А-ЯЁ]{1}[а-яё]+))?,\,{1,2}"
pattern2 = r"(8|\+7)?\s*\(?(\d{3})\)?\s*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d+)(?P<p>\s*)(\(*(?P<d>[доб]*\.)\s*(?P<n>\d+)\)*)*"
replace = r"\1,\2,\g<s>,"
replace2 = r"+7(\2)\3-\4-\5\g<p>\g<d>\g<n>"
best_contact = []
#Приведение к одному стандарту данных
for contact in contacts_list:
    result_contact = re.sub(pattern, replace, ','.join(contact))
    result_contact = re.sub(pattern2, replace2, result_contact)
    one_contact = re.split(",", result_contact)
    best_contact.append(one_contact)
#Объединение одинаковых контактов
counter = -1
for contact_comparison in best_contact:
    counter += 1
    counter2 = -1
    for comparison in best_contact:
        counter2 += 1
        if contact_comparison[0] == comparison[0] and contact_comparison[1] == comparison[1]:
            new_contact = [y if x=="" else x for x,y in zip(contact_comparison, comparison)]
            best_contact[counter] = new_contact
#Удаление дублей
temp = []
for x in best_contact: 
    if x not in temp:
        temp.append(x)
best_contact = temp
print('\nСтало')
pprint(best_contact)
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(best_contact)