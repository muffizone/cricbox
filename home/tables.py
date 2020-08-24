import django_tables2 as tables


class Scorecard(tables.Table):
    name = tables.Column(orderable=False)
    first_innings = tables.Column(orderable=False)
    second_innings = tables.Column(orderable=False)

    class Meta:
        template_name = "django_tables2/bootstrap.html"
