from rest_framework import serializers
from .models import TeamMember
from .utils import ChoiceField


class TeamMemberSerializer(serializers.ModelSerializer):
    role = ChoiceField(choices=TeamMember.ROLE_CHOICES)

    class Meta:
        model = TeamMember
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'role')
