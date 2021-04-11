from rest_framework import serializers
from apiApp import models

def start_with_r(value):
    if(value[0].lower()!='r'):
        raise serializers.ValidationError("name should start with r")

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=256,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=256)
    def create(self,validated_data):
        return models.Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
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