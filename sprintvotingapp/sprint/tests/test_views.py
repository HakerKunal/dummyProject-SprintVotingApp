import pytest, json
from rest_framework.reverse import reverse
from ..models import Sprint, Votes, Parameter
from user.models import User


@pytest.mark.django_db(transaction=True, reset_sequences=True)
class TestSprint:

    def test_add_sprint_by_non_root(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "False"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 401

    def test_add_sprint_by_root_user(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201

    def test_update_sprint_With_correct_sprint_id(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        updated_sprint_detail = {"is_active": "False"}
        url = reverse('update', kwargs={'id': 1})
        response = client.put(url, updated_sprint_detail, **header, content_type='application/json')
        assert response.status_code == 200

    def test_update_sprint_with_wrong_sprint_id(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        updated_sprint_detail = {"is_active": "False"}
        url = reverse('update', kwargs={'id': 10})
        response = client.put(url, updated_sprint_detail, **header, content_type='application/json')
        assert response.status_code == 404

    def test_delete_sprint_with_correct_sprint_id(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        url = reverse('update', kwargs={'id': 1})
        response = client.delete(url, **header, content_type='application/json')
        assert response.status_code == 200

    def test_delete_sprint_with_wrong_sprint_id(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        url = reverse('update', kwargs={'id': 11})
        response = client.delete(url, **header, content_type='application/json')
        assert response.status_code == 404

    def test_delete_sprint_by_non_root_user(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "False"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 401
        url = reverse('update', kwargs={'id': 1})

        response = client.delete(url, **header, content_type='application/json')
        assert response.status_code == 401

    def test_add_parameter_by_non_root_user(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "False"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        parameter_detail = {"parameter_name": "supportive"}
        url = reverse("add-parameter")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_detail, **header)
        assert response.status_code == 401

    def test_add_parameter_by_root_user(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        parameter_detail = {"parameter_name": "supportive"}
        url = reverse("add-parameter")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_detail, **header)
        assert response.status_code == 201

    def test_get_parameter_correct_id(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        parameter_detail = {"parameter_name": "supportive"}
        url = reverse("add-parameter")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_detail, **header)
        assert response.status_code == 201
        response = client.get(url, **header)
        assert response.status_code == 200

    def test_update_parameter_with_correct_id(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        parameter_detail = {"parameter_name": "supportive"}
        url = reverse("add-parameter")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_detail, **header)
        assert response.status_code == 201
        updated_parameter_detail = {"parameter_name": "Helping"}
        url = reverse("update-parameter", kwargs={'id': 1})
        response = client.put(url, updated_parameter_detail, **header, content_type='application/json')
        assert response.status_code == 200

    def test_update_parameter_with_wrong_id(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        parameter_detail = {"parameter_name": "supportive"}
        url = reverse("add-parameter")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_detail, **header)
        assert response.status_code == 201
        updated_parameter_detail = {"parameter_name": "Helping"}
        url = reverse("update-parameter", kwargs={'id': 2})
        response = client.put(url, updated_parameter_detail, **header, content_type='application/json')
        assert response.status_code == 404

    def test_delete_parameter_with_correct_id(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        parameter_detail = {"parameter_name": "supportive"}
        url = reverse("add-parameter")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_detail, **header)
        assert response.status_code == 201
        url = reverse("update-parameter", kwargs={'id': 1})
        response = client.delete(url, **header, content_type='application/json')
        assert response.status_code == 200

    def test_delete_parameter_with_wrong_id(self, client):
        user_detail = {
            "username": "usera123",
            "password": "usera123",
            "email": "kunalbatham15@gmail.com",
            "first_name": "user",
            "last_name": "batham",
            "is_verified": "True",
            "is_superuser": "True"

        }
        user = User.objects.create_user(username=user_detail.get("username"), password=user_detail.get("password"),
                                        email=user_detail.get("email"), first_name=user_detail.get("first_name"),
                                        last_name=user_detail.get("last_name"),
                                        is_verified=user_detail.get("is_verified"),
                                        is_superuser=user_detail.get("is_superuser"))
        user.save()
        data = {
            "username": "usera123",
            "password": "usera123",
        }
        url = reverse("login")
        response = client.post(url, data)

        assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        parameter_detail = {"parameter_name": "supportive"}
        url = reverse("add-parameter")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_detail, **header)
        assert response.status_code == 201
        url = reverse("update-parameter", kwargs={'id': 2})
        response = client.delete(url, **header, content_type='application/json')
        assert response.status_code == 404

    def test_vote_add_vote(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()
            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)

            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)

        json_data = json.loads(response.content)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 2
                },
                {
                    "parameter_id": 2,
                    "vote_to": 2
                },
                {
                    "parameter_id": 3,
                    "vote_to": 2
                },
                {
                    "parameter_id": 4,
                    "vote_to": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        json_data = json.loads(response.content)
        print(json_data)
        assert response.status_code == 201

    def test_vote_add_vote_for_myself(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()
            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)

            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)

        json_data = json.loads(response.content)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 1
                },
                {
                    "parameter_id": 2,
                    "vote_to": 1
                },
                {
                    "parameter_id": 3,
                    "vote_to": 1
                },
                {
                    "parameter_id": 4,
                    "vote_to": 1
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        json_data = json.loads(response.content)

        assert response.status_code == 400

    def test_vote_add_vote_for_invalid_user(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()
            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)

            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)

        json_data = json.loads(response.content)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 10
                },
                {
                    "parameter_id": 2,
                    "vote_to": 43
                },
                {
                    "parameter_id": 3,
                    "vote_to": 1
                },
                {
                    "parameter_id": 4,
                    "vote_to": 9
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')

        assert response.status_code == 400

    def test_vote_add_vote_for_invalid_parameter(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()
            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)

            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)

        json_data = json.loads(response.content)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 6,
                    "vote_to": 10
                },
                {
                    "parameter_id": 2,
                    "vote_to": 43
                },
                {
                    "parameter_id": 3,
                    "vote_to": 1
                },
                {
                    "parameter_id": 4,
                    "vote_to": 9
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 400

    def test_vote_get_result(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()
            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            json_data = json.loads(response.content)
            print(json_data)
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 2
                },
                {
                    "parameter_id": 2,
                    "vote_to": 2
                },
                {
                    "parameter_id": 3,
                    "vote_to": 2
                },
                {
                    "parameter_id": 4,
                    "vote_to": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.get(url, **header, content_type='application/json')
        assert response.status_code == 200

    def test_vote_wrong_sprint_id_result(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()

            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            json_data = json.loads(response.content)
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 2
                },
                {
                    "parameter_id": 2,
                    "vote_to": 2
                },
                {
                    "parameter_id": 3,
                    "vote_to": 2
                },
                {
                    "parameter_id": 4,
                    "vote_to": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        url = reverse("user-votes", kwargs={'id': 2})
        response = client.get(url, **header, content_type='application/json')
        assert response.status_code == 404

    def test_vote_update_vote(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userc123",
                "password": "userc123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userc",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()

            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            json_data = json.loads(response.content)
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 2
                },
                {
                    "parameter_id": 2,
                    "vote_to": 2
                },
                {
                    "parameter_id": 3,
                    "vote_to": 2
                },
                {
                    "parameter_id": 4,
                    "vote_to": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        vote_update_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 3
                },
                {
                    "parameter_id": 2,
                    "vote_to": 3
                },
                {
                    "parameter_id": 3,
                    "vote_to": 3
                },
                {
                    "parameter_id": 4,
                    "vote_to": 3
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.put(url, vote_update_data, **header, content_type='application/json')
        assert response.status_code == 200

    def test_vote_update_vote_self(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userc123",
                "password": "userc123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userc",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()

            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            json_data = json.loads(response.content)
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 2
                },
                {
                    "parameter_id": 2,
                    "vote_to": 2
                },
                {
                    "parameter_id": 3,
                    "vote_to": 2
                },
                {
                    "parameter_id": 4,
                    "vote_to": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        vote_update_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 1
                },
                {
                    "parameter_id": 2,
                    "vote_to": 1
                },
                {
                    "parameter_id": 3,
                    "vote_to": 1
                },
                {
                    "parameter_id": 4,
                    "vote_to": 1
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})

        response = client.put(url, vote_update_data, **header, content_type='application/json')
        assert response.status_code == 400

    def test_vote_update_vote_invalid_user(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userc123",
                "password": "userc123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userc",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()

            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)

            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            json_data = json.loads(response.content)
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 2
                },
                {
                    "parameter_id": 2,
                    "vote_to": 2
                },
                {
                    "parameter_id": 3,
                    "vote_to": 2
                },
                {
                    "parameter_id": 4,
                    "vote_to": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        vote_update_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 5
                },
                {
                    "parameter_id": 2,
                    "vote_to": 6
                },
                {
                    "parameter_id": 3,
                    "vote_to": 10
                },
                {
                    "parameter_id": 4,
                    "vote_to": 11
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.put(url, vote_update_data, **header, content_type='application/json')
        assert response.status_code == 400

    def test_vote_result(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()

            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            json_data = json.loads(response.content)
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 2
                },
                {
                    "parameter_id": 2,
                    "vote_to": 2
                },
                {
                    "parameter_id": 3,
                    "vote_to": 2
                },
                {
                    "parameter_id": 4,
                    "vote_to": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        url = reverse("result", kwargs={'id': 1})
        response = client.get(url, **header, content_type='application/json')
        assert response.status_code == 200

    def test_vote_result_wrong_sprint(self, client):
        list_of_user = [
            {
                "username": "usera123",
                "password": "usera123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "usera",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            },
            {
                "username": "userb123",
                "password": "userb123",
                "email": "kunalbatham15@gmail.com",
                "first_name": "userb",
                "last_name": "kumar",
                "is_verified": "True",
                "is_superuser": "True"
            }

        ]

        for users in list_of_user:
            user = User.objects.create_user(username=users.get("username"), password=users.get("password"),
                                            email=users.get("email"), first_name=users.get("first_name"),
                                            last_name=users.get("last_name"), is_verified=users.get("is_verified"),
                                            is_superuser=users.get("is_superuser"))
            user.save()

            data = {
                "username": "usera123",
                "password": "usera123",
            }
            url = reverse("login")
            response = client.post(url, data)

            assert response.status_code == 200
        json_data = json.loads(response.content)

        token = json_data.get('token')
        sprint_details = {"sprint_name": "practice sprint", "start_date": "2022-05-16", "end_date": "2022-05-30"}
        url = reverse("add")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_details, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }
            url = reverse("add-parameter")
            json_data = json.loads(response.content)
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "parameter_list": [
                {
                    "parameter_id": 1,
                    "vote_to": 2
                },
                {
                    "parameter_id": 2,
                    "vote_to": 2
                },
                {
                    "parameter_id": 3,
                    "vote_to": 2
                },
                {
                    "parameter_id": 4,
                    "vote_to": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        url = reverse("result", kwargs={'id': 2})
        response = client.get(url, **header, content_type='application/json')
        assert response.status_code == 404

