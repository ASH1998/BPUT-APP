__author__ = 'ASHU'

import scrapper

def get_roll(start_roll, num=1):
    try:
        new_roll = start_roll
        for i in range(num):
            print("scrapping for roll : ", new_roll)
            scrapper.main(new_roll)
            new_roll += 1

    except Exception as e:
        new_roll+=1
        print('Exception occured', e)
        get_roll(new_roll, num-i)


get_roll(1501105468, 20)

