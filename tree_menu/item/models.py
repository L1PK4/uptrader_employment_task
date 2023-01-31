from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.AutoField("item_id", unique=True, primary_key=True)
    name = models.CharField("name", max_length=50, unique=True)
    parent = models.ForeignKey("self", verbose_name="parent_id", null=True, on_delete=models.CASCADE)
    url = models.CharField("url", unique=True, max_length=50)

    def __str__(self):
        return self.name
    
    def __hash__(self) -> int:
        return hash(self.name)

    def get_children(self):
        return self.item_set.all()

    def get_path_to_root(self):
        # return Item.objects.raw(f'''
        #     WITH RECURSIVE parent_chain (id, name, parent_id) AS (
        #     SELECT id, name, parent_id
        #     FROM item_item
        #     WHERE id = {self.id}
        #     UNION
        #     SELECT i.id, i.name, i.parent_id
        #     FROM item_item i
        #     JOIN parent_chain pc ON i.id = pc.parent_id
        #     )
        #     SELECT par.id, array_agg(it.name) as children FROM parent_chain par
        #     right join item_item it on par.id = it.parent_id
        #     group by par.id
        #     having par.id is not null;
        # ''')
        return Item.objects.raw(f'''
            WITH RECURSIVE parent_chain (id, name, parent_id) AS (
            SELECT id, name, parent_id
            FROM item_item
            WHERE id = {self.id}
            UNION
            SELECT i.id, i.name, i.parent_id
            FROM item_item i
            JOIN parent_chain pc ON i.id = pc.parent_id
            )
            SELECT * FROM parent_chain;
        ''')
    
    
    