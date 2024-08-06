from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create initial users for different roles'

    def handle(self, *args, **kwargs):
        # Crear grupos si no existen
        admin_group, created = Group.objects.get_or_create(name='Administrador')
        agente_group, created = Group.objects.get_or_create(name='Agente de Campo')
        visualizador_group, created = Group.objects.get_or_create(name='Visualizador')

        # Crear usuarios
        if not User.objects.filter(username='admin').exists():
            user_admin = User.objects.create_user(username='admin', email='admin@example.com', password='adminpassword')
            user_admin.groups.add(admin_group)

        if not User.objects.filter(username='agente').exists():
            user_agente = User.objects.create_user(username='agente', email='agente@example.com', password='agentpassword')
            user_agente.groups.add(agente_group)

        if not User.objects.filter(username='visualizador').exists():
            user_visualizador = User.objects.create_user(username='visualizador', email='visualizador@example.com', password='viewerpassword')
            user_visualizador.groups.add(visualizador_group)

        self.stdout.write(self.style.SUCCESS('Successfully created initial users'))
