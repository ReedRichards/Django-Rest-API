from rest_framework import serializers
from core.models import AboutPage,Carousel,Press,Event,BlogPost,MakersNotes,ShopItem
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr

class UserSerializer(serializers.ModelSerializer):
    aboutpage = serializers.PrimaryKeyRelatedField(many=True, queryset=AboutPage.objects.all())

    class Meta:
        model = User
        fields =('id','username','aboutpage')


class AboutSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = AboutPage
        fields=('id','about_title','about_description','about_raw','owner')

class CarouselSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model=Carousel
        fields=('id','carousel_images','owner')

# http://blog.mathocr.com/2017/06/25/store-base64-images-with-Django-REST-framework.html
class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
            	# Break out the header from the base64 content
            	header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
            	decoded_file = base64.b64decode(data)
            except TypeError:
            	self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):

    	extension = imghdr.what(file_name, decoded_file)
    	extension = "jpg" if extension == "jpeg" else extension

    	return extension
class PressSerializers(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    press_image = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model=Press
        fields=('id','press_image','press_descritption','press_raw','owner')
                                    

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Event
        fields=(
            'id',
            'event_title',
            'event_start_date',
            'event_start_time',
            'event_end_date',
            'event_end_time',
            'event_details',
            'event_raw',
            'owner',
            'is_past_due',
            'is_multi_day'
        )

class BlogPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=BlogPost
        fields=('id','post_title','post_date','post_body','owner')

class MakersNotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=MakersNotes
        fields=(
            'id',
            'item_title',
            'item_description',
            'owner'
        )
class ShopItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model=ShopItem
        fields=(
            'id',
            'name',
            'image',
            'quantity',
            'price',
            'category',
            'description',
            'raw_description',
            'owner',
        )




class CreateUser(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields=('id','username','password')
