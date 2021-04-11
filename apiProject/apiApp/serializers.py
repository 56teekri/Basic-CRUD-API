from rest_framework import serializers
from apiApp import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields='__all__'
        read_only_fields=['roll']

    ######## Field Level Validation ########
    def validate_roll(self,value):
        if(value<1):
            raise serializers.ValidationError("Negative value nahi")
        if(value>50):
            raise serializers.ValidationError("Batch Full")
        return value

    ######## Object Level Validation ########
    def validate(self,data):
        name=data.get("name")
        city=data.get("city")
        if(name.lower() == 'radhe' and city.lower() != 'mathura'):
            raise serializers.ValidationError('City should be Mathura')
        return data 