from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

User=get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields={'id','email','username','create_at'}
        read_only_fields={'create_at',}

class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password=serializers.CharField(required=True,write_only=True,validators=[validate_password])
    confirm_pass=serializers.CharField(write_only=True,required=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'password','confirm_pass')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_pass']:
            raise serializers.ValidationError({'error':"Password fields didn't match"})
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        