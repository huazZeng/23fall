#algorithm
***
[toc]
***
##introduce
###goal
* solve problem
* efficience
* correctness 
* communicate to convince others
####algorithm
**f : input ---> ouput  (correctly)**
####efficiency
**instead of  measure real time, measure basic ops depend on the size of input**-->**O(n)** 

###data struction
####main  interface  
**problem**(what to store/what to do)
可以实现 以下数据结构
* set
* sequence

####main data struction **solution**(how to store/how to do)
* array
* pointer
#####static array  **const size**
get set len : O(1)
build interate : O(n)
insert in first and end:O(n)  ways: 1.shifting 2.allocate to extend the array
#####linked list
insert in first : O(1)
get set (i) : O(i) 

#####dynamic arrays
len size 
if len =size reallocate a new array *size >const x size*
**allocate** 
**amortization 摊销**
***
## set
#####data struction
* array 
* sorted array
compared by  build find insert delete find_min(max) find_next
### sorting
**input: n unordered numbers  --->output ordered sequence**
#### permutation sort 
列出所有可能并检查
O(n!)
#### selection sort
O(n2)
#### insert sort 
O(n2)
#### merge sort
O(n log n)
### Hashing











