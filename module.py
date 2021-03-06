import twstock
import requests
twstock.__update_codes()

#取得股名和及時股價
def get_price(stock_id):
    info=twstock.realtime.get(stock_id)
    if info['success']:
        return (info['info']['name'],info['realtime']['latest_trade_price'])
    else:
        return (False,False)
    
#依最佳四點取得買賣建議
def get_best(stock_id):
    stock=twstock.Stock(stock_id)
    bp=twstock.BestFourPoint(stock).best_four_point()
    if bp:
        return ('買進' if bp[0] else '賣出', bp[1])
    else:
        return (False,False)
    
#從csv檔讀取'股票代號','期望買進價','期望賣出價'
def get_setting():
    txt=input('text file name:')
    txt=txt +'.txt'
    res=[]
    try:
        with open(txt) as f:
            dlist=f.readlines()
            for lst in dlist:
                print(lst)
                s=lst.split(',')
                res.append([s[0].strip(),float(s[1]),float(s[2])])
    except:
        print(txt +'讀取錯誤')
    
    return res

#IFTTT發送訊息到LINE
def send_ifttt(v1,v2,v3):
    url=('https://maker.ifttt.com/trigger/toLINE/with/key/' +
         'mxYRhKKS3u9DvCAqR5rrrWr3glzMyg3QtWRpTQbi4nG' +
        '?value1=' + str(v1) +
        '&value2=' +str(v2) + 
        '&value3=' + str(v3))
    r=requests.get(url)
    if r.text[:5]=='Congr':
        print('已傳送(' + str(v1) + ', ' + str(v2) +', ' + str(v3) + ' )到LINE')
    else:
        print('errrror')
    return r.text

