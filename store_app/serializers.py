from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from store_app.models import User, Store
from store_app.permissions import IsAdmin

class UserSerializer(serializers.ModelSerializer):
    phonenumber = serializers.CharField(max_length=17, validators=[
        UniqueValidator(queryset=User.objects.all(), message="Phone number already exists.")
    ])
    password = serializers.CharField(write_only=True)

    def validate_phonenumber(self, value):
        # Check for 10 digits 
        if len(value.replace(" ", "")) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits long.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            phonenumber=validated_data['phonenumber'],
            store=validated_data['store'],
            code=validated_data['code'],
        )
        user.groups.set(validated_data['groups'])  # Use groups.set() to assign groups
        return user


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.phonenumber = validated_data.get('phonenumber', instance.phonenumber)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phonenumber', 'password', 'store', 'code', 'groups')
        extra_kwargs = {'password': {'write_only': True}}

class StoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store
        fields = '__all__'
        permissions_classes = [IsAdmin]