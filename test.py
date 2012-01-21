import loo

loo.app.config['DEBUG'] = True
#loo.models.create_all()
loo.app.run(host="0.0.0.0", port=3000)
