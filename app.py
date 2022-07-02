from web import app
from web.connector.scheduler import scheduler

if __name__ == "__main__":
    scheduler.start()
    app.run(debug=True, use_reloader=False, port=8080)  