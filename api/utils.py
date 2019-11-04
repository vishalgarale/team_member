from rest_framework import serializers


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        for i in self._choices:
            if self._choices[i] == data or str(i) == str(data):
                return i
        raise serializers.ValidationError("Acceptable values are {0}.".format(list(self._choices.values())))
