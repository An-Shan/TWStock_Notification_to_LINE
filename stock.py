import time 
import module as m

SList=m.get_setting()
count=len(SList) #計算所要查詢的股票數

log1=[]
log2=[]

for i in range(count):#對每支股票塞空字串為訊息
    log1.append('')
    log2.append('')
    
check_count=20 #檢查次數

while True:
    for i in range(count):
        id,low,high=SList[i]
        name,price=m.get_price(id)
        print('檢查:',name,'股價:',price,'區間:',low,'~',high)
        
        if float(price)<=low: #if及時股價到達期望買點
            if log1[i]!='買進':
                m.send_ifttt(name,price,'買進(股價低於 '+ str(low) + ')')
                log1[i]='買進'
                
        elif float(price)>=high: #if及時股價到達期望賣點
            if log1[i]!="賣出":
                m.send_ifttt(name,price,'買進(股價低於 '+ str(low) + ')')
                log1[i]='賣出'
        act,why=m.get_best(id)#檢查四大買點
        if why:
            if log2[i]!=why:#檢查前次訊息避免重複
                m.send_ifttt(name,price,act + '(' + why +')')
                log2[i]=why
    print('-------------------')
    
    check_count-=1
    if check_count==0:break
        
    time.sleep(180)#每3分鐘檢查一遍