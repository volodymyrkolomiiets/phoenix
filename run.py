# run.py
from application import create_app, db, models
from flask_migrate import Migrate
from flask import g
from flask.sessions import SecureCookieSessionInterface
from flask_login import user_loaded_from_cookie


app = create_app()
migrate = Migrate(app, db)


class CustomSessionInterface(SecureCookieSessionInterface):
    """ Prevent creating session from API requests. """
    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args, **kwargs)


app.session_interface = CustomSessionInterface()


@user_loaded_from_cookie.connect
def user_loaded_from_header(self, user=None):
    g.login_via_header = True


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
