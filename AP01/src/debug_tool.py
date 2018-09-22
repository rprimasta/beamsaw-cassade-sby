import inspect

class debug:
	def getClassMember(self,object):
        	for name, data in inspect.getmembers(object):
                	if name.startswith('__'):
                        	continue
                	print('{} : {!r}'.format(name, data))

