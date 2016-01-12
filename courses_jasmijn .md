```
Last login: Thu Nov 12 23:25:24 on console
LH-4:~ JasmijnK$ python
Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> [0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
>>> reeks = [0, 1, 2, 3, 4]
>>> reeks
[0, 1, 2, 3, 4]
>>> naam = "Jasmijn"
>>> naam
'Jasmijn'
>>> vakken = ["media design", "philosophy", "typography"]
>>> vakken
['media design', 'philosophy', 'typography']
>>> len(vakken)
3
>>> vakken.append("graphic design", "computer skills", "media theory"]
  File "<stdin>", line 1
    vakken.append("graphic design", "computer skills", "media theory"]
                                                                     ^
SyntaxError: invalid syntax
>>> vakken.append("graphic design", "computer skills", "media theory")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (3 given)
>>> vakken.append("graphic design")
>>> vakken 
['media design', 'philosophy', 'typography', 'graphic design']
>>> len(vakken)
4
>>> vakken = vakken + ["media theory", "crafts"]
>>> vakken 
['media design', 'philosophy', 'typography', 'graphic design', 'media theory', 'crafts']
>>> len(vakken)
6
>>> vakken.pop()
'crafts'
>>> vakken.pop()
'media theory'
>>> len(vakken)
4
>>> vakken
['media design', 'philosophy', 'typography', 'graphic design']
>>> del vakken [1]
>>> vakken
['media design', 'typography', 'graphic design']
>>> del vakken [3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> del vakken[2]
>>> vakken
['media design', 'typography']
>>> len(vakken)
2
>>>


```