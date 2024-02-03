from tastypie.authentication import ApiKeyAuthentication


# в класі ApiKeyAuthentication вже є метод is_authenticated
class CustomAuthentication(ApiKeyAuthentication):
    # is_authenticated - викликається для всіх методів крім GET
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        # super - викликає екзимпляр ApiKeyAuthentication і is_authenticated
        # викликається в нього
        return super().is_authenticated(request, **kwargs)
