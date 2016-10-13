from yi.observer import Observer

class Facade(object):
	instance = None
	ERROR_MESSAGE = ("Event name is None.")

	def __init__(self):
		self.observerMap = {}
		self.actorMap = {}

		self.initializeActor()

	@classmethod
	def getInstance(cls):
		if cls.instance is None:
			cls.instance = cls()
		return cls.instance

	def initializeActor(self):
		pass

	def registerObserver(self, event, observer):
		if event is None:
			raise EventNameError(self.ERROR_MESSAGE)

		if self.observerMap.get(event) is None:
			self.observerMap[event] = [observer]
		else:
			self.observerMap[event].append(observer)

	def notifyObservers(self, event, body={}):
		if event is None:
			raise EventNameError(self.ERROR_MESSAGE)

		observers_ = self.observerMap[event]
		if observers_:
			for i, v in enumerate(observers_):
				v.notifyObserver(event, body)

	def registerActor(self, actor):
		name = actor.name
		if self.actorMap.get(name):
			return

		self.actorMap[name] = actor

		interests = actor.listInterests()

		if interests:
			observer = Observer(actor.handleNotification, actor)
			for interest in interests:
				self.registerObserver(interest, observer)

		actor.onRegister()

	def getActor(self, name):
		self.actorMap.get(name)

	def send(self, event, body={}):
		self.notifyObservers(event, body)