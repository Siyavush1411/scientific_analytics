from django.db.models import Count, Avg, Max, Min, F
from apps.institution.models import Institution

class InstitutionWorkStatistic:
    
    @classmethod
    def get_institution_type_stats(cls):
        """Статистика по типам учреждений"""
        return list(
            Institution.objects
            .values('institution_type')
            .annotate(
                count=Count('id'),
                avg_rating=Avg('user__rating'),
                total_works=Count('user__scientific_work', distinct=True)
            )
            .order_by('-count')
        )
    
    @classmethod
    def get_top_institutions(cls, limit=5):
        """Топ учреждений по количеству работ"""
        return list(
            Institution.objects
            .annotate(total_works=Count('user__scientific_work'))
            .order_by('-total_works')[:limit]
            .values('name', 'total_works')
        )
