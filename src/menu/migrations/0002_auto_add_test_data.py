from django.db import migrations


def create_test_data(apps, schema_editor):
    Menu = apps.get_model("menu", "Menu")


    Menu.objects.create(name='Home', url='/', menu_name='main_menu')
    about = Menu.objects.create(name='About', url='/about/', menu_name='main_menu')
    Menu.objects.create(name='Contact', url='/contact/', menu_name='main_menu')

    Menu.objects.create(name='Team', url='/about/team/', parent=about, menu_name='main_menu')
    Menu.objects.create(name='History', url='/about/history/', parent=about, menu_name='main_menu')


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_test_data),
    ]
