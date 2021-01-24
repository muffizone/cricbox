# Django third party apps
import django_tables2 as tables


class FloatColumn(tables.Column):
    def render(self, value):
        return round(value, 2)


class SummingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return sum(bound_column.accessor.resolve(row) for row in table.data)
