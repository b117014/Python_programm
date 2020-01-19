## Set
- The set in python can be defined as the unordered collection of various items enclosed within the curly braces. The elements of the set can not be duplicate. The elements of the python set must be immutable.
- We can not direct access to the elemnt of set through index.
- use looping concept to get element from the set.

> Syntax

```python
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}  
print(Days)  
print(type(Days))  
print("looping through the set elements ... ")  
for i in Days:  
    print(i)  


```
>output
```python
{'Friday', 'Tuesday', 'Monday', 'Saturday', 'Thursday', 'Sunday', 'Wednesday'}
<class 'set'>
looping through the set elements ... 
Friday
Tuesday
Monday
Saturday
Thursday
Sunday
Wednesday
```