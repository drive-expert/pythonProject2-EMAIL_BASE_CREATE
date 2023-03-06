import csv

def list_files_name():
    import os
    os.chdir('csv')
    l_dir = os.listdir()
    print(l_dir)
    return l_dir

def remove_www(site_old):
    domain_new = str(site_old).replace('www.','') #убираем www.
    domain_new = domain_new.lower() #переводим в нижний регистр
    return domain_new

def domain_mass_create(site_file_name):
    prom = []
    domain_email = []
    domain_mass = {}
    with open(site_file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile) #читаем csv как словарь
        for row in reader:
            if len(row['Сайт']) > 1:
                row['Сайт'] = remove_www(str(row['Сайт']))
                row['Наименование'] = row['Наименование'].replace(',','')
                if row['Сайт'][:6] != 'vk.com':
                    domain_mass[str(row['Наименование'])] = domain_email = row['Сайт']
                    #print(row['Наименование'].replace(',',''))
                    #print(row['Сайт'])
    return domain_mass

def email_add_to_dict(domain_mass):
    for org_name in domain_mass:
        domain_mass[org_name] = domain_mass[org_name].append(f'info@{domain_mass[0]}')
        print(domain_mass[org_name])


#list_files_name()
email_add_to_dict(domain_mass_create('yp-ru-vologda.csv'))
