class heap():
    
    def __init__(self):
        self.items = []
       
        """Accepts two indexes of heap list as a parameter and swaps with each other.
        Returns nothing.The runtime for this method is O(1), or constant time.
        """
    def swap(self,s,i):
        temp = self.items[s]
        self.items[s]=self.items[i]
        self.items[i]=temp
  

        
        """Accepts index of heap list as a parameter and moves up in the heap
        list to correct position by swapping values with parent nodes.
        Returns nothing. The runtime for this method is O(log2 n) time.
        """                
    def shiftup(self,i):
        p = ((i-1)//2)
        if self.items[p][1] > self.items[i][1] and p >= 0:
            self.swap(p,i)
            self.shiftup(p)



        """Accepts index of heap list as a parameter and moves down in the heap
        list to correct position by swapping values with parent nodes.
        Returns nothing. The runtime for this method is O(log2 n) time.
        """        
    def shiftdown(self,i):
        c = 2*i + 1
        if c < (len(self.items) -1) and self.items[c+1][1] < self.items[c][1]:
            c = c+1            
        if c <= (len(self.items) -1) and self.items[i][1] > self.items[c][1]:
            self.swap(i,c)
            self.shiftdown(c)
    


        """Accepts value as a parameter and inserts in the end of heap
        list followed by shift up operation by swapping values with parent nodes.
        Returns nothing. The runtime for the insert operation is O(1) constant time 
        but shiftup method takes O(log2 n) time hence overall runtime is O(log2 n).
        """        
    def insert(self,i):
        self.items.append(i)     
        self.shiftup(len(self.items)-1)

    

        """Removes first value from the heap and brings the last value of the list
        to the first position followed by shift down operation to readjust the tree.
        Returns first value. The runtime for the delete operation is O(1) constant 
        time but shiftdown takes O(log2 n) time hence overall runtime is O(log2 n).
        """            
    def delmin(self):
        min=self.items[0]
        self.items[0]=self.items[-1]
        self.items.pop()
        self.shiftdown(0)
                
        return min



