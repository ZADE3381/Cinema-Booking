from app.main import app
from app.website import web

app.register_blueprint(web, url_prefix='/web')

if __name__ == "__main__": 
        app.run(debug=True)