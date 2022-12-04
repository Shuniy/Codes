def JosephusProblem(n, k):
    setMap = set(range(1, n + 1))
    return JosephusProblemHelper(n, k, 1, setMap)

def JosephusProblemHelper(n, k, start, setMap: set):
    if n == 1:
        return setMap
    
    toDelete = (start + k - 1)  % (n)
    setMap.remove(toDelete)
    return JosephusProblemHelper(n - 1, k, toDelete + 1, setMap)
    
def JosephusProblemEasy(n, k):
    if n == 1:
        return 1
    
    # After deleting one element, we will get last only element left
    afterDeletion = JosephusProblemEasy(n - 1, k)
    # We want to delete the Kth element in the remaining
    toDelete = afterDeletion + k - 1
    # After deleting that element, the safe element will be the next one to it.
    return (toDelete % n) + 1

n = 5
k = 2
print(JosephusProblem(n, k))
print(JosephusProblemEasy(n, k))

def Josh(person, k, index):
   
  # Base case , when only one person is left
  if len(person) == 1:
    print(person[0])
    return
   
  # find the index of first person which will die
  index = ((index+k)%len(person))
   
   # remove the first person which is going to be killed
  person.pop(index)
   
  # recursive call for n-1 persons
  Josh(person,k,index)
 
# Driver Program to test above function
n = 14 # specific n and k  values for original josephus problem
k = 2
k-=1   # (k-1)th person will be killed
 
index = 0
 
# fill the person vector
person=[]
for i in range(1,n+1):
  person.append(i)
 
Josh(person,k,index)