from turtle import pos
from django.dispatch import receiver
from django.db.models.signals import post_save
from PC.models import Usuario
from rolepermissions.roles import assign_role

@receiver(post_save, sender=Usuario)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.tipo == "S":
            assign_role(instance, 'auxiliar')
        elif instance.tipo == "A":
            assign_role(instance, 'administrador')
        else:
            assign_role(instance, 'administrador')
            obj = Usuario.objects.get(id = instance.id)
            obj.tipo = "A"
            obj.save()
            