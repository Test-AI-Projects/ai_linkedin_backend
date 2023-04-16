# authentication/views.py

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Use the built-in views for obtaining and refreshing tokens
token_obtain_pair = TokenObtainPairView.as_view()
token_refresh = TokenRefreshView.as_view()
