import random
import string
import names
import csv
import numpy as np
import os
class CsvHanlder:
    file_name = 'ilovecoffee'
    # if dir not exist, create it
    def __init__(self):
        if(not os.path.exists(self.file_name)):
            os.mkdir(self.file_name)

    # generate data
    def generate_data(self):
        # create a 2D array with 500 rows and 4 columns
        data = [[0]*4 for i in range(500)]
        data[0] = ['customer_id','customer_name', 'customer_mobile', 'frequency']
        
        for i in range(1,len(data)) :
            # generate customer_id
            data[i][0] =''.join([random.choice(string.ascii_letters) for n in range(1)]+[random.choice(string.ascii_letters+ string.digits) for n in range(7)])
            
            # generate frequency
            data[i][3] = random.randint(0,20)
        customer_name = [names.get_first_name() for i in range(10)]
        # generate customer_name
        for i in range(1,len(data)):
            data[i][1] =  random.choice(customer_name)+ '.' + data[random.randint(1,len(data)-1)][0]
        # generate customer_mobile
        phone_number = set([])
        while(len(phone_number)<len(data)-1):
            phone_number.add(''.join(['+8869']+[random.choice(string.digits) for n in range(8)]))
        # write customer_mobile to data
        for i in range(1,len(data)):
            data[i][2] = list(phone_number)[i-1]
        return data
    # write data to csv file
    def create_csv(self):
        with open(self.file_name+'/customers.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.generate_data())
    # calculate mean, median, mode
    def calculate(self):
        with open(self.file_name+'/customers.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            f=[]
            for row in reader:
                f.append(row[-1])
            f.pop(0)
            f = list(map(int,f))
            print('mean ={:.5f}'.format(np.mean(f)))
            print('median ={:n}'.format(np.median(f)))
            print('mode ={:n}' .format(max(set(f), key=f.count)))
    