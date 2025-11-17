#计算斯特林数 
tx=["n=0:1 ","n=1:0,1"]
tmp=[0,1]
n=8
#id=1
id=2

for i in range(2,n+1):
    row="n="+str(i)+":0,"
    tmp_next=[0]
            
    for j in range(1,i+1):
        if id==2:tmp_next.append( (tmp[j-1]+ tmp[j]*j) if j<i else 1 )
        elif id==1:tmp_next.append( (tmp[j-1]+ tmp[j]*(i-1)) if j<i else 1 )
        else:tmp_next.append( (tmp[j-1]+ tmp[j]) if j<i else 1 )
        row+= (str(tmp_next[-1])+",") if j<i else str(tmp_next[-1])
    tmp=tmp_next
    tx.append(row)
else:
    space_count=tx[n].split(',')
    tx_format=[tx[0].center(len(space_count[0]))]#格式化之后的tx
    print(tx_format[0])

    for k in range(1,n+1):
        tx_row=tx[k].split(',')
        row=''
        for j in range(k+1): row +=(',' if j>0 else '') + tx_row[j].center(len(space_count[j]))
        tx_format.append(row)
        print(row)
        