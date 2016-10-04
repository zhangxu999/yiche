#coding:utf-8

import json
import logging

def fixjson(data):
    '''
     pattern tha need to add '"""'

    { :
    , :
    ignore symbols
    ]
    }
    '''
    symbols = ',:{'
    cominbine = ['{:', ',:']
    index = [0, 0]
    stack = ''
    newdata = ''
    for i, x in enumerate(data):

        if x in symbols:
            if len(stack) == 0:
                stack += x;
                index[0] = i
            elif len(stack) == 1:
                stack += x;
                index[1] = i
                if stack in cominbine:
                    newdata = newdata[:-(index[1] - index[0] - 1)] + '"' + data[index[0] + 1:index[1]] + '"'
            else:
                stack = stack[1] + x
                index[0] = index[1]
                index[1] = i
                if stack in cominbine:
                    newdata = newdata[:-(index[1] - index[0] - 1)] + '"' + data[index[0] + 1:index[1]] + '"'
        newdata += x
    return newdata


def json2csv_chexing(chexing):
    # type: (object) -> object
    header = 'cur,url,num,type,id,name\n'
    ret = header

    data = json.loads(chexing)
    data = data['brand']

    for letter in data.keys():
        for car in data[letter]:
            ret += u','.join(map(lambda x: str(x), car.values()))
            ret += '\n'
    return ret.encode('utf-8')


def json2csv_chexing3(chexing):

    data = json.loads(chexing)
    logging.log(logging.DEBUG,len(data))
    for car in data:

        for feature in car:
            ret += ','.join(map(lambda x: '"'+str(x)+'"', feature))
            ret+=','
        ret += '\n'
    return ret
