from dataclasses import dataclass
from datetime import date
from typing import List, Dict, Any, Optional, Set

@dataclass
class ScoredTask:
    raw: Dict[str, Any]
    score: float
    priority_label: str
    explanation: str
    warnings: List[str]
    circular_dependency: bool

class PriorityScorer:
    def __init__(self, today: Optional[date] = None):
        self.today = today or date.today()

    def _urgency(self, d):
        if not d:
            return 0, "No due date"
        days = (d - self.today).days
        if days < 0:
            return 10, "Overdue"
        if days <= 1:
            return 9, "Due in 1 day"
        if days <= 3:
            return 7, "Due soon"
        if days <= 7:
            return 5, "Due in a week"
        return 2, "Low urgency"

    def _effort(self, hours):
        if hours <= 0.5:
            return 10, "Very small task"
        if hours <= 2:
            return 8, "Small task"
        if hours <= 4:
            return 6, "Medium task"
        return 4, "Big task"

    def _importance(self, imp):
        return imp, f"Importance {imp}/10"

    def _strategy_weights(self, s):
        s = (s or "smart_balance").lower()
        if s == "fastest_wins":
            return dict(urg=1, imp=1, eff=2.5)
        if s == "high_impact":
            return dict(urg=1, imp=3, eff=1)
        if s == "deadline_driven":
            return dict(urg=3, imp=1.5, eff=1)
        return dict(urg=2, imp=2, eff=1.5)

    def score(self, tasks, strategy="smart_balance"):
        weights = self._strategy_weights(strategy)
        out = []
        for t in tasks:
            urg_v, urg_t = self._urgency(t.get("due_date"))
            eff_v, eff_t = self._effort(t.get("estimated_hours", 1))
            imp_v, imp_t = self._importance(t.get("importance", 5))

            total = (
                weights["urg"] * urg_v +
                weights["imp"] * imp_v +
                weights["eff"] * eff_v
            )
            pr = "High" if total >= 22 else "Medium" if total >= 14 else "Low"
            expl = f"{urg_t}. {eff_t}. {imp_t}. Strategy={strategy}"
            out.append(ScoredTask(t, total, pr, expl, [], False))
        return sorted(out, key=lambda x: x.score, reverse=True)