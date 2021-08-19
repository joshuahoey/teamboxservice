from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone_number',
                  'start_date', 'address', 'tokens', 'image', 'is_employee']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            is_employee=validated_data['is_employee']
        )

        if validated_data['is_employee']:
            employee_group = Group.objects.get(name='Employees')
            employee_group.user_set.add(user)
        else:
            subscriber_group = Group.objects.get(name="Subscribers")
            subscriber_group.user_set.add(user)

        return user
