"""
a=list(map(int,input().split()))
page=[]
pagen=[]
dpages={}
for i in range(a[0]):
    x=list(map(str,input().split()))
    page.append(x[1:])
    pagen.append(x[0])
    dpages[x[0]]=0
#print(dpages)    
#print(page)
if(len(a)!=1):
    short=[]
    dshort={}
    for i in range(a[1]):
        x=list(map(str,input().split("~")))
        short.append(x)
        dshort[x[0]]=x[1]
    print(dshort)
    #print(short)
    mand=0
    while(mand<len(short)):
        for i in range(len(short)):
            if(short[i][-1] in dshort.keys()):
                x=dshort[short[i][-1]]
                #print(short[i])
                short[i][-1]=x
                #print("UP",short[i])
        mand+=1
    short_1=[]
    dshort_1={}
    for i in range(len(short)):
        if(short[i][-1] not in dshort.keys()):
            dshort_1[short[i][0]]=short[i][-1]
    print(dshort_1)
    pages=[]
    ref=["~","-","->",">"]
    id=[]
    for i in range(len(page)):
        for j in range(len(page[i])):
            tempor=" "
            tem=[]
            for k in range(len(page[i][j])-1):
                if(page[i][j][k] in ref and page[i][j][k+1] in ref): tempor=ref[ref.index(page[i][j][k])+1]
                elif(page[i][j][k] in ref): tempor=ref[ref.index(page[i][j][k])]
            x=[pagen[i]]
            for l in (page[i][j].split(tempor)):
                tem.append(l)
            if(tem[-1] in dshort_1.keys()):
                tem[-1]=dshort_1[tem[-1]]
                if(x[0]!=tem[-1]):
                    x.extend(tem)
                    pages.append(x)
                else:
                    id.append(tem[-1])
            elif(tem[-1] not in dshort.keys()):
                if(x[0]!=tem[-1]):
                    x.extend(tem)
                    pages.append(x)
    pages1=[]
    for i in pages:
        if(i[-1] not in id):
            pages1.append(i)
    print(id)        
    print(pages1)
    for i in pages1:
        x=dpages[i[-1]]
        x+=1
        dpages[i[-1]]=x
    print(dpages)
    ans=sorted(dpages.items(),key=lambda x: x[1])
    print(ans[-1][0])
    print(ans[-2][0])

else:
    #print(page)
    pages=[]
    ref=["~","-","->"]
    for i in range(len(page)):
        for j in range(len(page[i])):
            tempor=" "
            for k in page[i][j]:
                if(k in ref): tempor=ref[ref.index(k)]
            x=[pagen[i]]
            for l in (page[i][j].split(tempor)):
                x.append(l)
            pages.append(x)
    for i in pages:
        if(i[0]!=i[-1]):
            x=dpages[i[-1]]
            x+=1
            dpages[i[-1]]=x
    #print(dpages)
    ans=sorted(dpages.items(),key=lambda x: x[1])
    print(ans[-1][0])
    print(ans[-2][0])
    """

#updated latest
"""
a=list(map(int,input().split()))
inipage=[]
dpage={}
inishort=[]
dshort={}
if(len(a)!=1):
    for i in range(a[0]):
        x=list(map(str,input().split()))
        dpage[x[0]]=0
        tem=x[1:]
        sp=""
        #print("*******",tem)
        ref=["~","-","->",">"]
        for j in tem:
            temp=[x[0]]
            if(j!=[]):
                for k in range(len(j)-1):
                    if(j[k] in ref and j[k+1] in ref):sp=ref[ref.index(j[k])+1]
                    elif(j[k] in ref): sp=ref[ref.index(j[k])]
            for l in j.split(sp):
                temp.append(l)
            inipage.append(temp)
    temsh=[]
    for i in range(a[1]):
        x=list(map(str,input().split("~")))
        dshort[x[0]]=x[1]
        temsh.append(x)
    i=0
    while(i<len(temsh)):
        for j in temsh:
            if(j[-1] in dshort.keys()):
                x=dshort[j[-1]]
                j[-1]=x
        i+=1
    dshort1={}
    id=[]
    for j in temsh:
        if(j[-1] not in dshort.keys()):
            dshort1[j[0]]=j[1]
    for i in inipage:
        if(i[-1] not in dshort.keys() or i[-1] in dshort1.keys()):
            if(i[-1] in dshort1.keys() and i[-1] not in id):
                x=dshort[i[-1]]
                i[-1]=x
            if(i[-1]!=i[0] and i[-1] not in id):
                x=dpage[i[-1]]
                x+=1
                dpage[i[-1]]=x
            else:
                id.append(i[-1])
        else:id.append(i[-1])
    ans=sorted(dpage.items(),key=lambda x:x[1])
    print(ans[-1][0])
    print(ans[-2][0])
        


#print(inipage)
#print(dpage)

"""
a=int(input())
b=list(map(str,input().split()))
cost=0
for i in range(b.count("O")):
    for j in range(len(b)):
        count=b.count("X")
        if(b[j]=="O"):
            cost+=a
        else:
            cost+=(a-count)
            count-=1
    b[b.index("O")]="X"    
print("{0:.5f}".format(cost/a))