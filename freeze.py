import os
from flask_frozen import Freezer
from src.app import app

app.config['FREEZER_IGNORE_404_NOT_FOUND'] = True
app.config['FREEZER_DESTINATION'] = '../docs'
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def static():
    for dirpath, dirnames, filenames in os.walk(app.static_folder):
        for fname in filenames:
            # get path relative to the static directory
            rel = os.path.relpath(os.path.join(dirpath, fname),
                                  app.static_folder)
            # normalize for URLs on every OS
            rel = rel.replace(os.path.sep, '/')
            yield {'filename': rel}

if __name__ == '__main__':
    freezer.freeze()