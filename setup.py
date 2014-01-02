from setuptools import setup, find_packages

from herokuapp import __version__


version_str = ".".join(str(n) for n in __version__)
        

setup(
    name = "django-herokuapp",
    version = version_str,
    license = "BSD",
    description = "A set of utilities and a project template for running Django sites on heroku.",
    author = "Dave Hall",
    author_email = "dave@etianen.com",
    url = "https://github.com/etianen/django-herokuapp",
    entry_points = {
        "console_scripts": [
            "herokuapp_startproject = herokuapp.bin.herokuapp_startproject:main",
            "herokuapp_test = herokuapp.bin.herokuapp_test:main",
        ],
    },
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        "django",
        "pytz",
        "waitress",
        "dj-database-url",
        "psycopg2",
        "django-storages",
        "south",
        "boto",
        "sh",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)