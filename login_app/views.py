# from dj_rest_auth.views import LoginView


# class CustomLoginView(LoginView):


#     def get_response(self):
#         response = super().get_response()
#         remember_me = self.request.data.get('remember_me')
#         if remember_me:
#             self.request.session.set_expiry(60 * 60 * 24 * 3)  
#         else:
#             self.request.session.set_expiry(0)
#         return response