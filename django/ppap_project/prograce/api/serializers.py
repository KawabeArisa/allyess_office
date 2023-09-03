from rest_framework import serializers
from prograce.models import OrderListData, SupplierData, WorkNameData

class OLDPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderListData
        fields = ['id', 'PayTerms', 'Status', 'Supplier', 'WorkName', 'NumberEp', 'OrderDate', 'Money']

class SDPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierData
        fields = ['id', 'Code', 'Name']

class WNDPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkNameData
        fields = ['id', 'Code', 'Name']