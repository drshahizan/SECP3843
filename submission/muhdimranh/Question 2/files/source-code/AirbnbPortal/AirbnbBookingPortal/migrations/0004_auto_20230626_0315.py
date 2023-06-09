# Generated by Django 3.2.16 on 2023-06-25 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AirbnbBookingPortal', '0003_alter_listingandreviews_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingandreviews',
            name='accommodates',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='address',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='bed_type',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='beds',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='calendar_last_scraped',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='cancellation_policy',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='cleaning_fee',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='extra_people',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='first_review',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='guests_included',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='host',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='house_rules',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='images',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='interaction',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='last_review',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='last_scraped',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='maximum_nights',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='minimum_nights',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='number_of_reviews',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='price',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='property_type',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='review_scores',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='reviews',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='room_type',
        ),
        migrations.RemoveField(
            model_name='listingandreviews',
            name='security_deposit',
        ),
    ]
