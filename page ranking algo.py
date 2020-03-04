a,b=map(int,input().split())
page=[]
p=[]
short=[]
sh=[]
ans=[]
for i in range(a):
    x=list(map(str,input().split()))
    p.append(x[0])
    page.append(x[1:])
for i in range(b):
    x=list(map(str,input().split("~")))
    sh.append(x[0])
    short.append(x)
#print("page",page)
#print("short",short)
#print("p",p)
#print("sh",sh)
#print("*******************************************************************")
d1={}
for i in range(len(p)):
    d1[p[i]]=0
#print(d1)
#print("******************************************************************")
d2={}
for i in range(len(sh)):
    d2[sh[i]]=[short[i][-1]]
#print(d2)
#print("****************************************************************")
pages=[]
for i in range(len(p)):
    tem=[]
    for j in page[i]:
      x=[]
      tempor=j[2:-2]
      if(tempor=="->"):
        x.append(p[i])
        for m in (j.split("->")):
            x.append(m)
        tem.append(x)
      elif(tempor==">>"):
        x.append(p[i])
        for m in (j.split(">>")):
            x.append(m)
        tem.append(x)
        
      else:
        x.append(p[i])
        for m in (j.split("-")):
            x.append(m)
        tem.append(x)
        
    pages.append(tem)
#print("****",pages)
for i in range(len(sh)):
    for j in range(len(p)):
        for k in range(len(pages[j])):
            x=short[i][0]
            y=pages[j][k][-1]
            if(x==y):
                pages[j][k][-1]=short[i][-1]
#print(pages)
'''
for i in range(len(p)):
    for j in range(len(pages[i])):
        if(pages[i][j][-1] in d1.keys()):
            x=d1[pages[i][j][-1]]
            x.append(pages[i][j][0])
            d1[pages[i][j][-1]]=x
'''
#print(d1)
id=[]
tem1=0
while(tem1<len(sh)):
    for i in range(len(sh)):
        if(short[i][-1] in d2.keys()):
            short[i][-1]=d2[short[i][-1]][0]
    #print("UP",short)
    tem1+=1
id=[]
for i in range(len(short)):
    if(short[i][-1] in d2.keys()):
        id.append(i)
#print(id)
short1=[]
for i in range(len(short)):
    if(i not in id):short1.append(short[i])
#print(short)
#print(short1)  #shortlink updated
d2={}
for i in range(len(short1)):
    d2[short1[i][0]]=[short1[i][-1]]
#print("/*-*/",d2)
#print(d2.keys())
#print(d1.keys())
pages1=[]
for i in range(len(p)):
    tem=[]
    for j in range(len(pages[i])):
        if(pages[i][j][-1] in d1.keys()):
          #print(pages[i][j])
          tem.append(pages[i][j])
        if(pages[i][j][-1] in d2.keys()):
          #print(pages[i][j])
          tem.append(pages[i][j])
    pages1.append(tem)
#print(pages)
#print(pages1) #pages updated step:1
#print("******************************************************************")
id=[]
pages1_1=[]
for i in range(len(pages1)):
    tem=[]
    for j in range(len(pages1[i])):
        if(pages1[i][j][0]!=pages1[i][j][-1] and pages1[i][j][-1] not in id):
            tem.append(pages1[i][j])
        else:
            id.append(pages1[i][j][0])
    pages1_1.append(tem)
#print(pages1_1)
#print("///////////////",d1)
for i in range(len(pages1_1)):
    for j in range(len(pages1_1[i])):
        x=d1[pages1_1[i][j][-1]]
        x+=1
        d1[pages1_1[i][j][-1]]=x
#print(d1)
cc=0
for i in d1.values():
  if(i==0):
    cc+=1
if(cc!=len(d1)):
  ans=sorted(d1.items(),key=lambda x: x[1])
  print(ans[-1][0])
  print(ans[-2][0])
else:
  print("NO requisite")
            

