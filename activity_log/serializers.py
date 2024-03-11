from rest_framework import serializers
from activity_log.models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['user', 'type', 'description', 'store' ]
    
        
        