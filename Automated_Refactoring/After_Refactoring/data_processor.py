"""
Data Processing Module - Refactored with reusable aggregation engine.
"""

from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

Number = Union[int, float]


class DataProcessor:

    def _process_with_rules(
        self,
        data: Iterable[Any],
        rules: List[Tuple[type, Callable[[Any], Any], Callable[[Any], Number]]],
    ) -> Dict[str, Any]:
        processed: List[Any] = []
        total: Number = 0
        count = 0

        for item in data:
            for type_check, transform, measure in rules:
                if isinstance(item, type_check):
                    processed.append(transform(item))
                    total += measure(item)
                    count += 1
                    break

        avg = total / count if count > 0 else 0
        return {
            "processed": processed,
            "total": total,
            "average": avg,
            "count": count,
        }

    def process_numbers(self, data: Iterable[Any]) -> Dict[str, Any]:
        return self._process_with_rules(
            data,
            [((int, float), lambda x: x * 2, lambda x: x)],
        )

    def process_strings(self, data: Iterable[Any]) -> Dict[str, Any]:
        return self._process_with_rules(
            data,
            [(str, lambda s: s.upper(), lambda s: len(s))],
        )

    def process_mixed(self, data: Iterable[Any]) -> Dict[str, Any]:
        return self._process_with_rules(
            data,
            [
                ((int, float), lambda x: x * 2, lambda x: x),
                (str, lambda s: s.upper(), lambda s: len(s)),
            ],
        )

    def calc_stats(self, numbers: Iterable[Number]) -> Optional[Dict[str, Number]]:
        nums = list(numbers)
        if not nums:
            return None

        s = sum(nums)
        c = len(nums)
        a = s / c

        return {"sum": s, "count": c, "avg": a, "max": max(nums), "min": min(nums)}
