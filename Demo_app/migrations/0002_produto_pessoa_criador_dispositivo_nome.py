# Generated by Django 4.1 on 2022-09-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('adicionado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('codigo_produto', models.CharField(blank=True, max_length=30)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('categoria_tipo', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Variedades'), (3, 'Brinquedo'), (2, 'Comida')], null=True)),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
            },
        ),
        migrations.AddField(
            model_name='pessoa',
            name='criador_dispositivo_nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]