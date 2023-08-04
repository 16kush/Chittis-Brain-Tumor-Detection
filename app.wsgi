import os
import sys
from werkzeug.middleware.shared_data import SharedDataMiddleware

# Import your Flask app
from app import app

# Add shared data middleware to serve static files during development
app = SharedDataMiddleware(app, {
    '/static': app.config['UPLOAD_FOLDER']
})

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        from werkzeug.serving import run_simple

        extra_files = []
        for root, _, files in os.walk("templates"):
            for file in files:
                file_path = os.path.join(root, file)
                extra_files.append(file_path)

        run_simple('localhost', 5000, app, use_reloader=True, extra_files=extra_files)
    else:
        # For production, use a production-ready server like Gunicorn or uWSGI
        app.run()
