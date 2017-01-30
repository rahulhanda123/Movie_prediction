import re

test = 'E:JackandJill@twitter.com'

a = test.split(':')
user = a[1].split('@')
#print a[0]+':'+user[0][:1] + '*****' +user[0][-1:]+'@'+user[1]
test1 = 'P:+91(333)456-7890'
a1 = test1.split(':')
m = re.search(r'\((.*?)\)', a1[1])
n = re.search(r'\+(.*?)\(',a1[1])

if m is not None:
    print a1[0]+':'+'+'+ len(n.group(0)[1:-1])*'*'+'-'+len(m.group(1))*'*'+'-'+'***-'+a1[1][-4:]

