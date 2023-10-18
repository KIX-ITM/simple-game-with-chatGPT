from app import create_app as application

if __name__ == '__main__':
    app = application(config_mode='production')
    app.run()