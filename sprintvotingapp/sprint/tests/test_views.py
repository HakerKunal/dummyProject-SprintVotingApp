import pytest
from rest_framework.reverse import reverse
from ..models import Sprint, Votes, Parameter


@pytest.mark.django_db
class TestSprint:
    def test_user_registration(self, client):
        # test case create their own database to test the views
        url = reverse("registration")
        user = {
            "username": "kuna123",
            "password": "kuanl123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "kunal",
            "last_name": "batham",
        }
        response = client.post(url, user)

        assert response.status_code == 201
