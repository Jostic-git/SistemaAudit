from rest_framework import serializers

from ethiccertification.models import EthicItem, EthicItemAnswer3, EthicItemAnswer4, EthicItemAnswer2, EthicItemAnswer5


class EthicItemAnswer2Serializer(serializers.ModelSerializer):
    class Meta:
        model = EthicItemAnswer2
        fields = ['relation_status', 'FIO', 'share_of_capital', 'relation_to_corporation', 'company_name',
                  'company_INN', 'comment']


class EthicItemAnswer3Serializer(serializers.ModelSerializer):
    class Meta:
        model = EthicItemAnswer3
        fields = ['relation_status', 'FIO', 'comment']


class EthicItemAnswer4Serializer(serializers.ModelSerializer):
    class Meta:
        model = EthicItemAnswer4
        fields = ['relation_status', 'FIO', 'comment']


class EthicItemAnswer5Serializer(serializers.ModelSerializer):
    class Meta:
        model = EthicItemAnswer5
        fields = ['degree', 'FIO', 'position', 'impact', 'company', 'comment']


class EthicItemSerializer(serializers.ModelSerializer):
    ethic_item_answers_2 = EthicItemAnswer2Serializer(many=True)
    ethic_item_answers_3 = EthicItemAnswer3Serializer(many=True)
    ethic_item_answers_4 = EthicItemAnswer4Serializer(many=True)
    ethic_item_answers_5 = EthicItemAnswer5Serializer(many=True)

    class Meta:
        model = EthicItem
        fields = ['id', 'created', 'edited', 'company', 'employee', 'employee_position', 'status', 'answer_1',
                  'answer_1_comment', 'answer_2', 'ethic_item_answers_2', 'answer_3', 'ethic_item_answers_3',
                  'answer_4', 'ethic_item_answers_4', 'answer_5', 'ethic_item_answers_5', 'answer_6',
                  'answer_6_comment', 'answer_7', 'answer_7_comment', 'answer_8', 'answer_8_comment', 'answer_9',
                  'answer_9_comment', 'answer_10', 'answer_10_comment', 'questionnaire_file'
                  ]

    def create(self, validated_data):
        answers_2_data = validated_data.pop('ethic_item_answers_2')
        answers_3_data = validated_data.pop('ethic_item_answers_3')
        answers_4_data = validated_data.pop('ethic_item_answers_4')
        answers_5_data = validated_data.pop('ethic_item_answers_5')
        ethic_item = EthicItem.objects.create(**validated_data)
        for answer_2_data in answers_2_data:
            EthicItemAnswer2.objects.create(ethic_item=ethic_item, **answer_2_data)
        for answer_3_data in answers_3_data:
            EthicItemAnswer3.objects.create(ethic_item=ethic_item, **answer_3_data)
        for answer_4_data in answers_4_data:
            EthicItemAnswer4.objects.create(ethic_item=ethic_item, **answer_4_data)
        for answer_5_data in answers_5_data:
            EthicItemAnswer5.objects.create(ethic_item=ethic_item, **answer_5_data)
        return ethic_item
