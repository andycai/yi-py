from yi.facade import Facade

class Actor(object):
	def __init__(self, name):
		self.name = name

	def send(self, event, body):
		Facade.getInstance().notifyObservers(event, body)

	def listInterests(self):
		return []

	def handleNotification(self, event, body):
		pass

	def onRegister(self):
		pass

	def onRemove(self):
		pass