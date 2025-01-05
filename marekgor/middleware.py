from django.http import HttpResponseForbidden

class BlockSuspiciousPathsMiddleware:
    BLOCKED_PATHS = [
        "/wp-admin/", "/wp-content/", "/wp-includes/", "/.git/", "/wp-login.php",
        "/wp-config.php", "/.gitignore", "/.htaccess", "/readme.html", "/robots.txt",
        "/wp-json/", "/wp-cron.php", "/wp-load.php", "/wp-mail.php", "/wp-config-sample.php",
        "/.htpasswd", "/.htaccess.dist", "/.htaccess.sample", "/.htaccess.sample.php",
        "/.htaccess.sample.txt", "/.htaccess.sample.txt.php", "xmlrpc.php", "index.php",
        "/login/", "/user/", "/administrator/", "/joomla/", "/wordpress/",
        "/typo3/", "/drupal/", "/phpmyadmin/", "/marekgor/", "/cgi-bin/", "/server-status/",
        "/.well-known/", "/server-info/", "/config/", "/backup/", "/temp/", "/logs/",
        "/backup/", "/errors/", "/debug/", "/cache/", "/.env", "/__pycache__/",
        "/migrations/", "/.gitmodules", "/manage.py", "/db.sqlite3"
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        for path in self.BLOCKED_PATHS:
            if request.path.startswith(path):
                return HttpResponseForbidden("Forbidden")
        return self.get_response(request)
