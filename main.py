from yi.facade import Facade
import app

def main():
	Facade.getInstance().send(app.AppEvent.STARTUP)

if __name__ == '__main__':
	main()