from login_app.models import CustomUser
import pytest
import uuid
import secrets


@pytest.mark.django_db
def test_create_user_success():
    email = f"{uuid.uuid4().hex[:8]}@example.com"
    password = secrets.token_urlsafe(12)
    username = f"user_{uuid.uuid4().hex[:6]}"
    user = CustomUser.objects.create_user(email=email, password=password, username=username)
    assert user.email == email
    assert user.check_password(password)


def test_create_user_with_no_email():
    with pytest.raises(ValueError, match="Die E-Mail-Adresse muss angegeben werden"):
        CustomUser.objects.create_user(email=None, password="123")


@pytest.mark.django_db
def test_create_superuser_success():
    email = f"{uuid.uuid4().hex[:8]}@example.com"
    password = secrets.token_urlsafe(12)
    user = CustomUser.objects.create_superuser(email=email, password=password)
    assert user.is_staff is True
    assert user.is_superuser is True


def test_create_superuser_not_staff():
    with pytest.raises(ValueError, match="Superuser muss is_staff=True haben"):
        CustomUser.objects.create_superuser(email=f"{uuid.uuid4().hex[:8]}@example.com", password="123", is_staff=False)


def test_create_superuser_not_superuser():
    with pytest.raises(ValueError, match="Superuser muss is_superuser=True haben"):
        CustomUser.objects.create_superuser(email=f"{uuid.uuid4().hex[:8]}@example.com", password="123", is_superuser=False)


def test_str_method():
    username = str(uuid.uuid4())[:8]
    user = CustomUser(username=username)
    assert str(user) == username