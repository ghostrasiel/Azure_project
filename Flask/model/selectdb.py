import pymongo

def Mongo_start(): #主機啟動
    client=pymongo.MongoClient(host='localhost' , port=27017)
    return client

def Mongo_select(date):
    while True:
        try:
            client = Mongo_start()
            mydb = client.Azure
            collection = mydb.invoice
            json_data = collection.find_one({'Date':date} , {'_id':0})
            client.close()
            break
        except:
            pass
    return json_data

def Mongo_db_add(data): #把Azure加入至資料
    while True:
        try:
            client = Mongo_start()
            mydb = client.Azure
            collection = mydb.invoice
            # collection.drop()
            collection.insert(data)
            client.close()
            print('OK!')
            break
        except:
            pass

def Mongo_db_select(): #查詢最後中獎發票的月份
    while True:
        try:
            client = Mongo_start()
            mydb = client.Azure
            collection = mydb.invoice
            if collection.find_one() != None:
                result = collection.aggregate([{'$group':
                {"_id":"$item" , 'maxDate':{'$max':"$Date"}}
                }])
                client.close()
                start_Date =''
                for i in result:
                    start_Date = str(i['maxDate'])
            else :
                client.close()
                start_Date  = None
            break
        except:
            pass
    return start_Date