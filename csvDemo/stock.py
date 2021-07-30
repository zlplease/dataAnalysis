# coding=utf8

import csv

def read_csv_stock():
    with open('stock.csv','r',encoding='utf-8') as fp:
        reader = csv.reader(fp)
        next(reader)
        for x in reader:
            name = x[3]
            volumn = x[-1]
            print({'name':name,'volumn':volumn})

def read_csv_stock1():
    with open('stock.csv','r',encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        for x in reader:
            value = {"name":x['secShortName'],'volumn':x['turnoverVol']}
            print(value)

def write_csv_classRoom():
    headers = ['username', 'age', 'height']
    values = [
    ('吴振溢',18,170),
    ('胡鑫',19,170),
    ('周浩东',18,170)
    ]
    with open('classroom.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

def write_csv_classRoom2():
    headers = ['username', 'age', 'height']
    values = [
    {'username':'吴振溢','age':18,'height':170},
    {'username':'胡鑫','age':19,'height':170},
    {'username':'周浩东','age':18,'height':170}
    ]
    with open('classroom.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.DictWriter(fp,headers)
        writer.writeheader()
        writer.writerows(values)



if __name__ == '__main__':
    write_csv_classRoom2()