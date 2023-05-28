def merge_the_tools(string,k):
  import textwrap
  l=textwrap.wrap(string,k)
  for i in l:
    d=list(i[::-1])
    g=set(i)
    for t in g:
      for e in range(1,i.count(t)):
        d.remove(t)
    print(''.join(d[::-1]))