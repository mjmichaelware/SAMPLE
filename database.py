import sqlite3
from flask import g

def get_db():
    if 'db' not in g:
            g.db = sqlite3.connect(
                        get_app().config['DATABASE'],
                                    detect_types=sqlite3.PARSE_DECLTYPES
                                            )
                                                    g.db.row_factory = sqlite3.Row
                                                        return g.db

                                                        def close_db(e=None):
                                                            db = g.pop('db', None)
                                                                if db is not None:
                                                                        db.close()

                                                                        def init_db(app):
                                                                            with app.app_context():
                                                                                    db = get_db()
                                                                                            with open('schema.sql', 'r') as f:
                                                                                                        db.executescript(f.read())
                                                                                                            app.teardown_appcontext(close_db)

                                                                                                            def get_app():
                                                                                                                from .__init__ import app as current_app
                                                                                                                    return current_app