-bash-4.2$ python3
Python 3.6.8 (default, Apr 25 2019, 21: 02: 35)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.

>> > test_list = ['bangalore', 'chennai', 'mangalore', 'vizag', 'delhi']
>> > print(test_list.index('bangalore'))
0
>> > test_list_1 = [1, 2, 3, 4, 5]
>> > print(test_list_1.index(4))
3

#OR

-bash-4.2$ python3
Python 3.6.8 (default, Apr 25 2019, 21:02:35)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> test_list = ['bangalore','chennai','mangalore','vizag','delhi']
#finds the item 'bangalore' only within 0th to 3rd element in list and returns the index
>>> print(test_list.index('bangalore',0,3))
0


#finds the item 'bangalore' only within 1st to 3rd element in list and returns the index, and since the item 'bangalore' is not in that range, we get the exception
>>> print(test_list.index('bangalore',1,3))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'bangalore' is not in list
>>>

#OR
Python 3.6.8 (default, Apr 25 2019, 21:02:35)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> test_list = ['bangalore','chennai','mangalore','vizag','delhi']
>>> print(test_list.index('bhopal'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'bhopal' is not in list
>>>
