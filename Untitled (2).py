#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[33]:


num = int(input())
row_num = num*2
space_handler=0
star_handler=0
first_loop_sp=0
first_loop_st=1
if num%2!=0:  
    for i in range(1,row_num+1):
        if i <=num+num//2:
            for j in range(num):
                print(' ',end='')
        else:
            for j in range(num//2-first_loop_sp):
               print(' ',end='')
            
            for j in range(first_loop_st):
                print('*',end='')
            for j in range(num//2-first_loop_sp):
               print(' ',end='')
       
        if i<=num:
             if i <= num//2+1:
                if i!=1:
                  space_handler+=1 
                  star_handler+=2
             else:
                space_handler-=1 
                star_handler-=2
             for j in range(space_handler):
                print(' ',end='')
             for j in range(num-star_handler):
                 print('@',end='')
        else:
            for j in range(num):
                if j==0 or j==num-1:
                    print('@',end='')
                else:print(' ',end='')
        if i <=num+num//2:
            for j in range(num):
                print(' ',end='')
        else:
            for j in range(num//2-first_loop_sp):
               print(' ',end='')
            
            for j in range(first_loop_st):
                print('*',end='')
            first_loop_st+=2
            for j in range(num//2-first_loop_sp):
               print(' ',end='')
            first_loop_sp+=1
            
                    
        
                
                
            
        
       
        print()


# In[ ]:





# In[ ]:




