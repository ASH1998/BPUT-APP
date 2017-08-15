__author__ = 'ASHU'

import scrapper
import json
import os

def get_roll(start_roll, num=1):
    fileName = 'sem3_json.json'
    try:
        new_roll = start_roll
        for i in range(num):
            print("scrapping for roll : ", new_roll)
            dict_1 = scrapper.main(new_roll)
            new_roll += 1
            if os.path.exists(fileName):
                write_append = 'a'
            else:
                write_append = 'w'
            
            with open(fileName, write_append) as f:
                json_text = json.dumps(dict_1, indent=3)
                f.write("{}\n".format(json_text))

    except Exception as e:
        new_roll+=1
        print('Exception occured', e)
        get_roll(new_roll, num-i)


get_roll(1501105468, 10)

