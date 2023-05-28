st="aimsn soeruwslio oeaaeingsdpt crthio rbodthf yxit oei flo fea rooemhmgph aehnohy oesl ng aey oecblj ingloe aejeaw eatho boey cfcj lae n thp ux oexg pfseoaeoe ingpeooea gaeioingtho paoethringae csbeoyh txelr gwy jfiniocyeaiio oth ecaecxioea olc frdingeu dcleasxcgio wsth fding iiomaaeg ws nd cpthxpeaea wu eaw fwjy xdwcgcoe dxoe riog npayp cyh fejean oeae ua hr eeathfja lxst mflft gith ulg xeatsljp lxi".upper()
print(st,st.count('A'))
print("lenght: ",len(st))
freq=[0 for i in range(26)]
for j in range(len(st)):
    if st[j].isalpha():
        freq[ord(st[j])-65]+=1
for j in range(26):
    print(f"{chr(65+j)}: {freq[j]}")

# st.replace()