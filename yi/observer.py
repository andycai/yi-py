class Observer(object):
	def __init__(self, notifyMethod, notifyContext):
		self.notify = notifyMethod
		self.context = notifyContext

	def notifyObserver(self, event, body):
		self.notify(event, body)