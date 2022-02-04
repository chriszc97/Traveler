from rest_framework import serializers
from .models import Country, Destination


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    destinations = serializers.HyperlinkedRelatedField(
        view_name='destination_detail',
        many=True,
        read_only=True
    )

    country_url = serializers.ModelSerializer.serializer_url_field(
        view_name='country_detail'
    )

    class Meta:
        model = Country
        fields = ('id', 'name', 'photo_url', 'destinations', 'country_url',)


class DestinationSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.HyperlinkedRelatedField(
        view_name='country_detail',
        read_only=True
    )
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source='country'
    )

    class Meta:
        model = Destination
        fields = ('country_id', 'name', 'photo_url', 'description',
                  'food', 'landmarks', 'cost', 'country',)
