from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_item_name'),
    ]
    operations = [
        migrations.RunSQL(
            sql="""INSERT INTO item_item 
                        (id, name, url, parent_id)
                        VALUES 
                            (1, 'Animal', '/item/Animal/', null),
                            (2, 'Chordata', '/item/Chordata/', 1),
                            (3, 'Porifera', '/item/Porifera/', 1),
                            (4, 'Mammalia', '/item/Mammalia/', 2),
                            (5, 'Calcarea', '/item/Calcarea/', 3),
                            (6, 'Elephantidae', '/item/Elephantidae/', 4),
                            (7, 'Felis catus', '/item/Felis_catus/', 4),
                            (8, 'Figure', '/item/Figure/', null),
                            (9, 'Polygon', '/item/Polygon/', 8),
                            (10, 'Convex polygon', '/item/Convex_polygon/', 9),
                            (11, 'Triangle', '/item/Triangle/', 10),
                            (12, 'Quadrilateral', '/item/Quadrilateral/', 10),
                            (13, 'Square', '/item/Square/', 12);
                """,
            reverse_sql="DELETE FROM app_model;"
        )
    ]
