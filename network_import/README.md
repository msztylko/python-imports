# Network Import

Sometimes it's useful to execute code from the network and this is relatively easy to do in Python. For that we need 3 things:
1. [source_code.py](./source_code.py) - python source code that prints current time when executed.
2. [source_server.py](./source_server.py) - minimal HTTP server that serves `source_code.py` on request.
3. [client.py](./client.py) - minimal client that requests source code from server.

## Next steps
How can we modify client so that still gets source code from the network, but hidding this entire process behind `import source_code` ?
