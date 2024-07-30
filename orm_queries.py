from app1.models import Order, Store
from django.db.models import Count, Sum, Case, When
from django.db import connection, reset_queries




# cost of all of orders
Order.objects.aggregate(Sum("cost"))

# number of orders per store
Order.objects.values("store").annotate(Count("cost"))

# sum of orders per store
Order.objects.values("store").annotate(Sum("cost"))

# using select related to optimize database connection
Order.objects.select_related("store").values("store__name").annotate(Count("cost"))

# using Case When in conditaional expressions
Order.objects.annotate(
        large_order=Case(When(cost__gte=20000, then=True), default=False)
    ).values("id", "large_order")