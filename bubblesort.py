
def bubbleSort(numList):
  for j in range(len(numList)-1,0,-1): # going backwards
    
    for i in range(j):
      #print("           ", numList)
      
      if numList[i] > numList[i + 1]:
        
        temp = numList[i]  # swap
        
        numList[i] = numList[i + 1]
        numList[i + 1] = temp
        
        #print("After swap:", numList)
        #print()
        
    #print("Checked thru the list\n")
  return numList
  
  
numList = [6,1,5,10,2,4,3,9,7,8]

print(bubbleSort(numList))
  

# runtime: O(n^2)




""" minimal code
def bubbleSort(numList):
  for j in range(len(numList)-1, 0, -1): # goes backwards
    for i in range(j):
      
      if numList[i] > numList[i+1]:
        temp = numList[i]
        
        numList[i] = numList[i+1]
        numList[i+1] = temp
        
  return numList"""
