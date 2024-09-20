from rest_framework import serializers
from .models import TeamInfo, User, Player, Waiver 

class TeamInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInfo 
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player 
        fields = '__all__'

class WaiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiver 
        fields = '__all__'
