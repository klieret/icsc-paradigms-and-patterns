class Class:
	def method(self):
		# needs to be called from INSTANCE and can access instance attributes
	@classmethod
	def classmethod(cls):
		# no access to instance attributes

# This won't work:
Class.method()  # <-- needs an instance, e.g. Class(...).method()

# But this does:
Class.classmethod()
