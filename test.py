import loo

loo.app.config['DEBUG'] = True

from loo import views

loo.app.run(host="0.0.0.0", port=3000)
