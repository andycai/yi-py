from yi.actor import Actor
from app import AppEvent

class RoleActor(Actor):
	EVENT_ROLE_SHOW_NICK = "EVENT_ROLE_SHOW_NICK"

	def __init__(self):
		super(RoleActor, self).__init__("role_actor")

	def listInterests(self):
		return [AppEvent.STARTUP, RoleActor.EVENT_ROLE_SHOW_NICK]

	def handleNotification(self, event, body):
		print "-------------la la la, event:" + event