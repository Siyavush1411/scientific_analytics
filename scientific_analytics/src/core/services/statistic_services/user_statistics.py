from django.db.models import Count, Avg
from apps.users.models import User

class UserWorkStatistic:
    
    @classmethod
    def get_user_status_stats(cls):
        """Статистика пользователей по статусам"""
        return list(
            User.objects
            .values('status__status_name')  # исправлено
            .annotate(
                count=Count('id'),
                avg_rating=Avg('rating'),
                avg_works=Count('scientific_work')
            )
            .order_by('-count')
        )
    
    @classmethod
    def get_institution_users_stats(cls):
        """Статистика пользователей по учреждениям"""
        return list(
            User.objects
            .values('institution__name')
            .annotate(
                users_count=Count('id'),
                avg_rating=Avg('rating'),
                total_works=Count('scientific_work')
            )
            .order_by('-users_count')
        )
    
    @classmethod
    def get_top_users(cls, limit=5):
        """Топ пользователей по рейтингу"""
        return list(
            User.objects
            .order_by('-rating')[:limit]
            .values(
                'username', 
                'rating', 
                'institution__name',
                works_count=Count('scientific_work')
            )
        )
    
    @classmethod
    def get_user_work_distribution(cls):
        """Распределение количества работ среди пользователей"""
        return list(
            User.objects
            .annotate(works_count=Count('scientific_work'))
            .values('works_count')
            .annotate(users_count=Count('id'))
            .order_by('works_count')
        )
