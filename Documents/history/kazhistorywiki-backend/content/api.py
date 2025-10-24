from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Category, Person, Event, Comment ,HistoricalPeriod
from .serializers import CategorySerializer, PersonSerializer, EventSerializer ,CommentSerializer,HistoricalPeriodSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(categories__id=category_id)
        return queryset
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HistoricalPeriodViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPeriod.objects.all()
    serializer_class = HistoricalPeriodSerializer