from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskInputSerializer
from .scoring import PriorityScorer

@api_view(["POST"])
def analyze_tasks(request):
    data = request.data
    tasks = data.get("tasks", [])
    strategy = data.get("strategy", "smart_balance")

    s = TaskInputSerializer(data=tasks, many=True)
    s.is_valid(raise_exception=True)
    tasks_valid = s.validated_data

    scorer = PriorityScorer()
    scored = scorer.score(tasks_valid, strategy)

    result = []
    for t in scored:
        d = dict(t.raw)
        d.update({
            "score": t.score,
            "priority": t.priority_label,
            "explanation": t.explanation
        })
        result.append(d)

    return Response({
        "strategy": strategy,
        "results": result
    })

@api_view(["POST"])
def suggest_tasks(request):
    data = request.data
    tasks = data.get("tasks", [])
    strategy = data.get("strategy", "smart_balance")

    s = TaskInputSerializer(data=tasks, many=True)
    s.is_valid(raise_exception=True)

    scorer = PriorityScorer()
    scored = scorer.score(s.validated_data, strategy)

    top = scored[:3]
    result = []
    for t in top:
        d = dict(t.raw)
        d.update({
            "score": t.score,
            "priority": t.priority_label,
            "explanation": t.explanation
        })
        result.append(d)

    return Response({
        "strategy": strategy,
        "top_3": result
    })