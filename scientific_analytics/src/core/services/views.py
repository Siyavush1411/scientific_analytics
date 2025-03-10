# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .statistic_services.institution_statistocs import InstitutionWorkStatistic
from .statistic_services.science_work_statistic import ScientificWorkStatistics
from .statistic_services.user_statistics import UserWorkStatistic

class InstitutionStatsAPI(APIView):
    def get(self, request):
        return Response({
            'types': InstitutionWorkStatistic.get_institution_type_stats(),
            'top_institutions': InstitutionWorkStatistic.get_top_institutions()
        })

class ScientificWorkStatsAPI(APIView):
    def get(self, request):
        return Response({
            'general': ScientificWorkStatistics.get_general_stats(),
            'categories': ScientificWorkStatistics.get_category_stats(),
            'top_works': ScientificWorkStatistics.get_top_works()
        })

class UserStatsAPI(APIView):
    def get(self, request):
        return Response({
            'statuses': UserWorkStatistic.get_user_status_stats(),
            'top_users': UserWorkStatistic.get_top_users(),
            'work_distribution': UserWorkStatistic.get_user_work_distribution()
        })