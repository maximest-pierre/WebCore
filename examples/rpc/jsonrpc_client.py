try:
    import jsonrpclib
except ImportError:
    print 'You need to install jsonrpclib to run this example.'
    raise


server = jsonrpclib.Server('http://localhost:8080', version='1.0')

print server.test.hello()
print server.test.hello('JSON-RPC')
