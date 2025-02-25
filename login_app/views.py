# from dj_rest_auth.views import LoginView
# from django.conf import settings


# class CustomLoginView(LoginView):


#     def get_response(self):
#         response = super().get_response()
#         remember_me = self.request.data.get('remember_me')
#         token = response.data.get("key")


#         if token:
#             if remember_me:
#                 max_age = 60 * 60 * 24 * 3
#             else:
#                 max_age = None
#             response.set_cookie(key="auth_token", value=token, httponly=True, secure=settings.SESSION_COOKIE_SECURE, samesite="Lax", max_age=max_age)


#         return response
    

#         response = super().get_response()
#         remember_me = self.request.data.get('remember_me')
#         if remember_me:
#             self.request.session.set_expiry(60 * 60 * 24 * 3)  
#         else:
#             self.request.session.set_expiry(0)
#         return response