import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as pl

#выделить функции, оптимизировать
def grafic(spisok):#полная жесть, все нафиг переделать
    print(spisok.keys())
    gg=range(195,40,-5)
    for n in range(1,23+1):
        pl.text(27,gg[n], str(n)+'.', size="xx-small")
    f=5
    for n in range(24,46+1):
        pl.text(37,195-f, str(n)+'.', size="xx-small")
        f+=5
    print(195-f)
    f=5
    for el in spisok:
        if (195-f)== 75:
            break
        pl.text(28.5, 195-f, el, size = "xx-small")
        f+=5
    f = 5
    h=-110
    for el in spisok:
        if (195 + f) > 310:

           pl.text(38.5, 195 - h, el, size="xx-small")
        h+=5
        f += 5
    x = spisok.values()
    y = np.arange(len(x))
    width = .8
    l=range(1,len(spisok)+1)
    rgb = np.array([0, 70, 155]) / 255
    plt.bar(y,x, width, align='center', color=rgb)
    plt.xticks(y,l)
    plt.title('Histogram of senders')
    plt.ylabel('Number of messeges')
    plt.xlabel("№ sender's name")
    return plt.show()
def countMsg(dic,key):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1
    return None
def spamAverage(text,listSpam):
    i=0
    sum=0
    count=0
    for line in text:
        l = line.split(':')
        if l[0]=='X-DSPAM-Confidence':
            listSpam.append(float(l[1]))
            sum+=float(l[1])
            count+=1
            i+=1
    mid=sum/count
    return mid
def main():
    with open('mbox.txt', 'r') as mail:
        senderList={}
        name=[]
        spam=[]
        blackList={}
        average = spamAverage(mail, spam)
        print('Average value of X-DSPAM-Confidence: ', average)
        mail.seek(0)
        for line in mail:
           line=line.strip()
           if line.startswith('From '):
                line=line.split()
                name.append(line[1])
                countMsg(senderList,line[1])
    i=1
    blackList[name[0]] = [spam[0]]
    while i < int(len(spam)):
        if not name[i] in blackList:
            blackList[name[i]]=[spam[i]]
        else:
            blackList[name[i]].append(spam[i])
        i+=1
    print('BlackList: ',blackList)
    sel=0
    f = open('spam.txt', 'w')
    for i in blackList:
        numberSpamMsg=len(blackList[i])
        for n in range(numberSpamMsg):
            value=blackList.setdefault(i)[n]
            if value>average:
                sel+=1
        if sel*100/numberSpamMsg > 50:
            #print('Spamer:',i,'Value:',sum(spam_dict.setdefault(i))/all,'%:',sel*100/all, 'Number:',spisok[i] )
            f.write('Spamer: '+ i+'          Value: '+ str(sum(blackList.setdefault(i)) / numberSpamMsg)+  '\t'+' %: '+ str(sel * 100 / numberSpamMsg)+ '\t'+' Number: '+ str(senderList[i])+'\n')
        #   print('Spamer: ',i,'Value:','Sel: ', sel*100/all,'*',sum(spam_dict.setdefault(i)/float(all)))
        sel=0
    f.close()
    grafic(senderList)
if __name__==('__main__'):
    main()

