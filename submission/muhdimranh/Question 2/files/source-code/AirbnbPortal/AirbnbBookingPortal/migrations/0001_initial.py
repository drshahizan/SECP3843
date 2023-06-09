# Generated by Django 3.2.16 on 2023-06-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListingAndReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=255)),
                ('listing_url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('interaction', models.TextField()),
                ('house_rules', models.TextField()),
                ('property_type', models.CharField(max_length=255)),
                ('room_type', models.CharField(max_length=255)),
                ('bed_type', models.CharField(max_length=255)),
                ('minimum_nights', models.CharField(max_length=255)),
                ('maximum_nights', models.CharField(max_length=255)),
                ('cancellation_policy', models.CharField(max_length=255)),
                ('last_scraped', models.DateField()),
                ('calendar_last_scraped', models.DateField()),
                ('first_review', models.DateField()),
                ('last_review', models.DateField()),
                ('accommodates', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('number_of_reviews', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amenities', models.JSONField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('security_deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cleaning_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('extra_people', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guests_included', models.DecimalField(decimal_places=2, max_digits=10)),
                ('images', models.JSONField()),
                ('host', models.JSONField()),
                ('address', models.JSONField()),
                ('availability', models.JSONField()),
                ('review_scores', models.JSONField()),
                ('reviews', models.JSONField()),
            ],
        ),
    ]
