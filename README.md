# python-imports
Exploration of the Python import system

# [The import system](https://docs.python.org/3/reference/import.html)

**Importing** - process by which Python code in one module gains access to the code in another module.

There are 3 main ways to perform import:
1. `import` statement - the most common way
```python
>>> import sys
>>> 're' in sys.modules
False
>>> import re
>>> 're' in sys.modules
True
```
2. `importlib.import_module()`
```python
>>> import sys
>>> 're' in sys.modules
False
>>> import importlib
>>> importlib.import_module('re')
<module 're' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/re.py'>
>>> 're' in sys.modules
True
```
3. built-in `__import__()`
```python
>>> import sys
>>> 're' in sys.modules
False
>>> __import__('re', globals(), locals(), [], 0)
<module 're' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/re.py'>
>>> 're' in sys.modules
True
```

Conceptuallu, we may say that `import` statement performs 2 operations:
1. search for the named module.
2. bind the result to a name in the local scope.

Search operation (1.) is defined as a call to the `___import__()` function. Return value is used to perform the name binding. `sys.modules` is updated as a side-effect, by name binding is performed only by `import` statement. 

Compare `import` statement
``` python
>>> import re
>>> re
<module 're' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/re.py'>
```
with `__import__()` function
```python
>>> __import__('re', globals(), locals(), [], 0)
<module 're' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/re.py'>
>>> re
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 're' is not defined
```

The second point about binding in the **local scope** can be illustrated with:
```python
>>> def func():
...     print(f'{globals()=}')
...     print(f'{locals()=}')
...     import re
...     print(f'{globals()=}')
...     print(f'{locals()=}')
... 
>>> func()
globals()={'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'func': <function func at 0x104f8c9d0>}
locals()={}
globals()={'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'func': <function func at 0x104f8c9d0>}
locals()={'re': <module 're' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/re.py'>}
>>> re
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 're' is not defined
```
Only local scope of function `func` is updated with variable `re`. We get a NameError when we try to access `re` from the global scope.
