stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99,
         'email': 42, 'ok': 98}

company_sale = []

for company, sale in stats.items():
    company_sale.append(sale)

max_company_sale = max(company_sale)

for company, sale in stats.items():
    if sale == max_company_sale:
        print(f'Канал "{company}" с максимальным объемом продаж '
              f'{max_company_sale} единиц')



