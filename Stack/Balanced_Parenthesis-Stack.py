def bal_par(s):
    op={"(":0,"{":1,"[":2}
    cl={")":0,"}":1,"]":2}
    st=[]
    for i in s:
        if i in op:
            st.append(i)
        else:
            if len(st)>0 and op[st[-1]]==cl[i]:
                st.pop()
            else:
                return "NO"
    if len(st)==0:
        return "YES"
    return "NO"
inp=input("Enter Value")
print(bal_par(list(inp)))