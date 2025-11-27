from rest_framework import serializers

class TaskInputSerializer(serializers.Serializer):
    id = serializers.CharField(required=False, allow_blank=True)
    title = serializers.CharField()
    due_date = serializers.DateField(required=False, allow_null=True)
    estimated_hours = serializers.FloatField(required=False)
    importance = serializers.IntegerField(min_value=1, max_value=10)
    dependencies = serializers.ListField(
        child=serializers.CharField(), required=False
    )

    def validate(self, data):
        if "estimated_hours" not in data:
            data["estimated_hours"] = 1.0
        if "dependencies" not in data:
            data["dependencies"] = []
        return data