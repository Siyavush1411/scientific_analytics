from django.db.models import Count, Avg, Max, Min, F
from apps.scientific_work.models import ScientificWork

class ScientificWorkStatistics:
    
    @classmethod
    def get_general_stats(cls):
        """Общая статистика по научным работам"""
        return ScientificWork.objects.aggregate(
            total_works=Count('id'),
            avg_rating=Avg('work_rating'),
            avg_uniqueness=Avg('uniquenes_score'),
            max_rating=Max('work_rating'),
            min_rating=Min('work_rating')
        )
    
    @classmethod
    def get_category_stats(cls):
        """Статистика по категориям"""
        return list(
            ScientificWork.objects
            .values('category__category_name')
            .annotate(
                count=Count('id'),
                avg_rating=Avg('work_rating'),
                avg_uniqueness=Avg('uniquenes_score')
            )
            .order_by('-count')
        )
    
    @classmethod
    def get_top_works(cls, limit=5, by='work_rating'):
        """Топ работ по указанному критерию"""
        return list(
            ScientificWork.objects
            .order_by(f'-{by}')[:limit]
            .values('work_name', 'work_rating', 'uniquenes_score', 'author__username')
        )
