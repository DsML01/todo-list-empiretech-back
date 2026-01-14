from todo_list_empiretech_back import create_app
from todo_list_empiretech_back.settings import settings

app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0', port=settings.FLASK_PORT, debug=settings.FLASK_DEBUG
    )
