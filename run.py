__author__ = 'tauren'

# from app import create_app
from restless_app import create_app

app = create_app('../testing.cfg')
app.run(debug=True)

