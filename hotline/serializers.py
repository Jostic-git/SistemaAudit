from rest_framework import serializers
from hotline.models import HotLineItem, HotLineFile, HotLineComment, SubCategoryHotLine, CategoryHotLine


class CategoryHotLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryHotLine
        fields = ['id', 'title']


class SubCategoryHotLineSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title')

    class Meta:
        model = SubCategoryHotLine
        fields = ['id', 'company', 'category', 'category_name', 'title', 'responsible_employee']


class HotLineFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotLineFile
        fields = ['id', 'hotline_item', 'file']


class HotLineCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotLineComment
        fields = ['id', 'hotline_item', 'comment', 'created', 'user_name']


class HotLineItemSerializer(serializers.ModelSerializer):
    hotline_files = HotLineFileSerializer(many=True, read_only=True)
    hotline_comments = HotLineCommentSerializer(many=True, read_only=True)
    subcategory_title = serializers.CharField(source='sub_category.title', read_only=True)

    class Meta:
        model = HotLineItem
        fields = ['id', 'company', 'created', 'received', 'channel', 'sub_category', 'subcategory_title',
                  'received_text', 'client_contact',
                  'forwarded', 'forwarded_to_emp', 'status', 'status_answer', 'action', 'damage', 'hotline_files',
                  'hotline_comments', 'closed']
