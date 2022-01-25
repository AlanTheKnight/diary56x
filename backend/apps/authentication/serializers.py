from rest_framework import serializers

from . import models


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for `Student` model."""

    class Meta:
        model = models.Student
        exclude = ["account"]


class TeacherSerializer(serializers.ModelSerializer):
    """Serializer for `Teacher` model."""

    class Meta:
        model = models.Teacher
        exclude = ["account"]


class UserSerializer(serializers.ModelSerializer):
    """Serializer for `User` model."""

    options_student = StudentSerializer()
    options_teacher = TeacherSerializer()

    class Meta:
        model = models.User
        fields = [
            "id",
            "account_type",
            "email",
            "first_name",
            "second_name",
            "surname",
            "registration_date",
            "last_login",
            "options_student",
            "options_teacher",
            "is_superuser",
            "is_staff",
            "is_active",
        ]
        read_only_fields = [
            "id",
            "account_type",
            "is_superuser",
            "is_staff",
            "is_active",
        ]


class CompactUserSerializer(serializers.ModelSerializer):
    """Serializer for `User` model."""

    class Meta:
        model = models.User
        fields = [
            "id",
            "email",
            "first_name",
            "second_name",
            "surname",
            "is_superuser",
            "is_staff",
            "account_type",
        ]
        read_only_fields = ["id"]


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "account_type",
            "email",
            "first_name",
            "second_name",
            "surname",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = models.User.objects.create(
            account_type=validated_data["account_type"],
            surname=validated_data["surname"],
            first_name=validated_data["first_name"],
            second_name=validated_data["second_name"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "account_type",
            "email",
            "first_name",
            "second_name",
            "surname",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = models.User.objects.create(
            account_type=validated_data["account_type"],
            surname=validated_data["surname"],
            first_name=validated_data["first_name"],
            second_name=validated_data["second_name"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserBulkDeleteSerializer(serializers.Serializer):
    ids = serializers.CharField()


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
