import time 
import module as m

SList=m.get_setting()
count=len(SList) #�p��ҭn�d�ߪ��Ѳ���

log1=[]
log2=[]

for i in range(count):#��C��Ѳ���Ŧr�ꬰ�T��
    log1.append('')
    log2.append('')
    
check_count=20 #�ˬd����

while True:
    for i in range(count):
        id,low,high=SList[i]
        name,price=m.get_price(id)
        print('�ˬd:',name,'�ѻ�:',price,'�϶�:',low,'~',high)
        
        if float(price)<=low: #if�ήɪѻ���F����R�I
            if log1[i]!='�R�i':
                m.send_ifttt(name,price,'�R�i(�ѻ��C�� '+ str(low) + ')')
                log1[i]='�R�i'
                
        elif float(price)>=high: #if�ήɪѻ���F������I
            if log1[i]!="��X":
                m.send_ifttt(name,price,'�R�i(�ѻ��C�� '+ str(low) + ')')
                log1[i]='��X'
        act,why=m.get_best(id)#�ˬd�|�j�R�I
        if why:
            if log2[i]!=why:#�ˬd�e���T���קK����
                m.send_ifttt(name,price,act + '(' + why +')')
                log2[i]=why
    print('-------------------')
    
    check_count-=1
    if check_count==0:break
        
    time.sleep(180)#�C3�����ˬd�@�M