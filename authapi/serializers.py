from django.core.exceptions import ValidationError
from rest_framework import serializers
from authapi.models import models
#for sending a password reset link to email
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.db.auth.tokens import PasswordResetTokenGenerator

from account.utils import Util