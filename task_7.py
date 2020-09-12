import sys
import json

def _main():
    """Entry point."""
    with open('text_7.txt', encoding='utf-8') as f_obj:
        companies_data = list()
        for line in f_obj:
            company_data = line.split()
            company_data[2] = int(company_data[2])
            company_data[3] = int(company_data[3])
            company_profit = company_data[2] - company_data[3]
            company_data.append(company_profit)
            companies_data.append(company_data)

    companies_profit = 0
    profitable_companies = 0
    for element in companies_data:
        if element[-1] > 0:
            profitable_companies += 1
            companies_profit += element[-1]

    average_profit = companies_profit / profitable_companies
    average_profit = dict(average_profit=average_profit)
    companies = dict()
    for company in companies_data:
        companies.update({company[0]: company[-1]})
    result = [companies, average_profit]
    
    with open('text_7.json', 'w', encoding='utf-8') as json_obj:
        json.dump(result, json_obj, ensure_ascii=False)


if __name__ == '__main__':
    sys.exit(_main())