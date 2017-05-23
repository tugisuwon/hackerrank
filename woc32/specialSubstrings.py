#/bin/python

class Node:
    def __init__(self,length,suffix,i0=-1):
        self.length = length
        self.suffix = suffix
        self.rev_suffixes = []
        self.nextp = [0]*26
        self.i0 = i0
    def __repr__(self):
        return 'length={},suffix={},rev_suffixes={},nextp={}'.format(self.length,self.suffix,self.rev_suffixes,self.nextp)

def propertyOfString(s):
    num = 2 #index of the latest added node
    suff = 2 #current largest palindromic suffix
    tree[1] = Node(-1,1)
    tree[2] = Node(0,1)
    result = []
    cur_result = 0
    for i,c in enumerate(s):
        let = ord(c)-ord('a')
        cur = suff
        while (True):
            curlen = tree[cur].length
            if (i-1-curlen>=0 and s[i-curlen-1]==c):
                break
            cur = tree[cur].suffix
        if (tree[cur].nextp[let]):
            suff = tree[cur].nextp[let]
            result.append(cur_result)
            continue
        num += 1
        suff = num
        tree[num].length = tree[cur].length + 2
        tree[num].i0 = i-tree[num].length+1
        tree[cur].nextp[let] = num
        if (tree[num].length == 1):
            tree[num].suffix = 2
            tree[2].rev_suffixes.append(num)
            cur_result += 1
            result.append(cur_result)
            continue
        
        while (True):
            cur = tree[cur].suffix
            curlen = tree[cur].length
            if (i - 1 - curlen >= 0 and s[i - 1 - curlen] == s[i]):
                tree[num].suffix = tree[cur].nextp[let]
                parent_node = tree[tree[num].suffix]
                coinciding_so_far = [True]*len(parent_node.rev_suffixes)
                for j in range(parent_node.length,i-tree[num].i0+1):
                    all_chars_different = True
                    for sb,sibling in enumerate(parent_node.rev_suffixes):
                        if coinciding_so_far[sb] and j<tree[sibling].length and s[tree[num].i0+j]==s[tree[sibling].i0+j]:                            
                            all_chars_different = False
                        else:
                            coinciding_so_far[sb] = False
                    if all_chars_different:
                        #print('cur_result={},j={},tree[num].length={}'.format(cur_result,j,tree[num].length))
                        cur_result += (tree[num].length-j)
                        break
                tree[tree[num].suffix].rev_suffixes.append(num)
                result.append(cur_result)
                break
    return result
       #import random
#n=3*10**5
#s=''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(n)])
#s='racecarenterelephantmalayalam'
#print(s)
n = int(raw_input().strip())
s = raw_input().strip()
#s = 'daddgdbgbdaghhgdbbdb'
#s = 'dbdbbd'
n = len(s)
tree = [Node(-1,1) for _ in range(n+3)]
 
result = propertyOfString(s)
for r in result:
    print(r)

