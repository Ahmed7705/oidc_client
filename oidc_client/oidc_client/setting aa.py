# Security Settings

# Enforce HTTPS for secure communications
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # Enable HSTS for one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Cookies security
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Strict'

# Clickjacking protection
X_FRAME_OPTIONS = 'DENY'

# Content Security Policy (CSP)
CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = ["'self'"]
CSP_STYLE_SRC = ["'self'"]
CSP_IMG_SRC = ["'self'"]
CSP_CONNECT_SRC = ["'self'"]
CSP_FONT_SRC = ["'self'"]
CSP_OBJECT_SRC = ["'none'"]
CSP_BASE_URI = ["'none'"]
CSP_FRAME_ANCESTORS = ["'none'"]

# Limit access to admin panel
ADMIN_IP_WHITELIST = ['127.0.0.1']  # Example for localhost only

# Logging of suspicious activities
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'security_warnings.log'),
        },
    },
    'loggers': {
        'django.security': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

# Token security
DEFAULT_TOKEN_LIFETIME = 3600  # Example: 1 hour

# Middleware to enforce security policies
MIDDLEWARE.insert(0, 'django.middleware.security.SecurityMiddleware')

# CORS settings
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [
    'https://trusted-domain.com',  # Add trusted domains only
]
CORS_ALLOW_CREDENTIALS = True

# Rate limiting (install and configure django-ratelimit)
RATELIMIT_VIEW = 'app_name.views.ratelimited_view'
RATELIMIT_KEY = 'user_or_ip'
RATELIMIT_METHODS = ['POST']  # Example for sensitive actions only

# Authentication and access control
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Use django-axes for brute-force attack prevention
INSTALLED_APPS += ['axes']
MIDDLEWARE += ['axes.middleware.AxesMiddleware']
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1  # Example: 1 hour
