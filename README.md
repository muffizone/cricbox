[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# London Fields website
This Django project has been created for storing statistics, information and reports for a cricket club.

## Quick start

The django application is broken down into the following individual apps.

Theoretically this structure can be reused across any clubs with a similar format without much changes.

    batsman
    bowler
    home
    match
    match_statistics
    opposition
    player
    venue

### Environment Variables Settings
Set the following environment variables before starting the application:
```
export DJANGO_SETTINGS_MODULE=cricbox.settings
export DJANGO_CRICBOX_PATH=<path-to-django-root-directory>
export DJANGO_SECRET_KEY=<secret-key>
export DJANGO_DB_DATABASE=<db-username>
export DJANGO_DB_HOSTNAME=<db-host>
export DJANGO_DB_USERNAME=<db-username>
export DJANGO_DB_PASSWORD=<db-password>
export DJANGO_SENTRY_URL=<sentry-url>
```
