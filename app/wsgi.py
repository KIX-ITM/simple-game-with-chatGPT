from app import create_app as application

if __name__ == '__main__':
    application = application(config_mode=None)
    application.run()