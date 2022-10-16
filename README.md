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
