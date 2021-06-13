from setuptools import setup

setup(
    name = 'django-sage-painless',         # How you named your package folder (MyLib)
    packages = ['sage_painless'],   # Chose the same as "name"
    version = '0.1.1',      # Start with a small number and increase it with every change you make
    license='GNU',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'django package for auto generating projects',   # Give a short description about your library
    author = 'Sage Team',                   # Type in your name
    author_email = 'mail@sageteam.org',      # Type in your E-Mail
    url = 'https://github.com/sageteam-org/django-sage-painless',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/sageteam-org/django-sage-painless/archive/refs/tags/0.3.tar.gz',    # I explain this later on
    keywords = ['django', 'python', 'generate', 'code generator'],   # Keywords that define your package best
    install_requires=[
        'Django',
        'django-redis',
        'redis',
        'drf-yasg',
        'django-seed',
        'Faker'
    ]
)