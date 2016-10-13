from yi.facade import Facade

class AppEvent(object):
	STARTUP = "STARTUP"
	
	def __init__(self):
		pass

from app.modules.role.actor import RoleActor
Facade.getInstance().registerActor(RoleActor())
