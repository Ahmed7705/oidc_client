import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-zm-2f26!3=3lln*o+m@$yj@o&s#olmk_dlw%m5uw(03gh^gzij'

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oidc_client_app',
    'sslserver'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oidc_client.urls'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

SESSION_COOKIE_SECURE = False  
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oidc_client.wsgi.application'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Client Settings

OIDC_SERVER_URL = 'http://127.0.0.1:8010/oidc/'
CLIENT_ID = '123'
CLIENT_SECRET = '456'

REDIRECT_URI = 'https://localhost:8011/oidc-client/test-access/'

# OIDC Server URLs
OIDC_AUTHORIZATION_URL = 'http://localhost:8010/oidc/authorize/'
OIDC_TOKEN_URL = 'http://localhost:8010/oidc/token/'
OIDC_USERINFO_URL = 'http://localhost:8010/oidc/userinfo/'



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
ADMIN_IP_WHITELIST = ['127.0.0.1']

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
    'https://127.0.0.1'
    'http://localhost',
    'http://127.0.0.1'  
]
CORS_ALLOW_CREDENTIALS = True

# Rate limiting (install and configure django-ratelimit)
RATELIMIT_VIEW = 'oidc_client_app.views.ratelimited_view'
RATELIMIT_KEY = 'user_or_ip'
RATELIMIT_METHODS = ['POST']  

# Authentication and access control
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'axes.backends.AxesStandaloneBackend',  

]

# Use django-axes for brute-force attack prevention
INSTALLED_APPS += ['axes']
MIDDLEWARE += ['axes.middleware.AxesMiddleware']
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
