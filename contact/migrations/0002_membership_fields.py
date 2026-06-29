from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactmessage",
            name="university",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="contactmessage",
            name="session",
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name="contactmessage",
            name="union_name",
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name="contactmessage",
            name="village",
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name="contactmessage",
            name="school",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="contactmessage",
            name="college",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="contactmessage",
            name="phone",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="contactmessage",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name="contactmessage",
            name="message",
            field=models.TextField(blank=True),
        ),
    ]
