from .models import SampleData

from rest_framework import serializers

class SampleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SampleData
		fields = ['id', 'name', 'lat', 'lon']
