# C:\Users\ahmed\Desktop\SSO Project\SSO\oidc_client\oidc_client\oidc_client_app\views.py
from django.http import JsonResponse
from requests_oauthlib import OAuth2Session
from django.conf import settings
from django.shortcuts import redirect

from django.contrib.auth.decorators import  permission_required


import secrets
import hashlib
import base64

def generate_pkce_pair():
    code_verifier = secrets.token_urlsafe(64)

    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).decode().rstrip('=')

    return code_verifier, code_challenge

code_verifier, code_challenge = generate_pkce_pair()


def oidc_login(request):
    oidc = OAuth2Session(
        client_id=settings.CLIENT_ID,
        redirect_uri=settings.REDIRECT_URI,
        scope=['openid', 'profile', 'email']
    )
    
    authorization_url, state = oidc.authorization_url(
        settings.OIDC_AUTHORIZATION_URL,
        code_challenge=code_challenge,
        code_challenge_method="S256" 
    )

    authorization_url += f"&custom_state={state}"
    

    return redirect(authorization_url)



def oidc_callback(request):
    state = request.GET.get('state')
    if not state:
        return JsonResponse({'error': 'State is missing'}, status=400)

    print("Received state:", state)

    oidc = OAuth2Session(
        client_id=settings.CLIENT_ID,
        redirect_uri=settings.REDIRECT_URI,
        state=state
    )
    token = oidc.fetch_token(
    settings.OIDC_TOKEN_URL,
    client_secret=settings.CLIENT_SECRET,  
    code=request.GET.get('code'),
    code_verifier=code_verifier,
    authorization_response=request.build_absolute_uri()
)

    # token = oidc.fetch_token(
    #     settings.OIDC_TOKEN_URL,
    #     client_secret=settings.CLIENT_SECRET,
    #     authorization_response=request.build_absolute_uri()
    # )

    userinfo = oidc.get(settings.OIDC_USERINFO_URL).json()

    return JsonResponse({'userinfo': userinfo})


# @login_required
@permission_required('oidc_client_app.view_resource', raise_exception=True)
def test_access_view(request):
    return JsonResponse({'message': 'المستخدم لديه صلاحية الوصول إلى الموارد.'})

def no_access_view(request):    
    return JsonResponse({'message': '22المستخدم لا يملك الصلاحية للوصول إلى الموارد.'}, status=403)
z       