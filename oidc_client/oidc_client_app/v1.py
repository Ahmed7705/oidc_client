
# from django.http import JsonResponse
# from requests_oauthlib import OAuth2Session
# from django.conf import settings
# from django.shortcuts import redirect


# from django.shortcuts import redirect
# from requests_oauthlib import OAuth2Session
# from django.conf import settings

# def oidc_login(request):
#     oidc = OAuth2Session(
#         client_id=settings.CLIENT_ID,
#         redirect_uri=settings.REDIRECT_URI,
#         scope=['openid', 'profile', 'email']
#     )
#     authorization_url, state = oidc.authorization_url(settings.OIDC_AUTHORIZATION_URL)
#     # إرسال state مع redirect_uri
#     authorization_url += f"&custom_state={state}"


#     # # تخزين state في الجلسة
#     # request.session['oidc_state'] = state
#     # print("State saved in session:", state)


#     return redirect(authorization_url)



# def oidc_callback(request):
#     state = request.GET.get('state')
#     if not state:
#         return JsonResponse({'error': 'State is missing'}, status=400)

#     print("Received state:", state)

#     oidc = OAuth2Session(
#         client_id=settings.CLIENT_ID,
#         redirect_uri=settings.REDIRECT_URI,
#         state=state
#     )
#     token = oidc.fetch_token(
#         settings.OIDC_TOKEN_URL,
#         client_secret=settings.CLIENT_SECRET,
#         authorization_response=request.build_absolute_uri()
#     )

#     # استرجاع معلومات المستخدم باستخدام Access Token
#     userinfo = oidc.get(settings.OIDC_USERINFO_URL).json()

#     return JsonResponse({'userinfo': userinfo})
