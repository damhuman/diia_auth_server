import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


# Get the version
from diia_auth_server import __version__


def get_long_description():
    readme = ""

    with open('README.md', encoding='utf-8') as readme_file:
        readme = readme_file.read()

    return readme


REQUIREMENTS_FOLDER = os.getenv('REQUIREMENTS_PATH', '')
requirements = [line.strip() for line in open(os.path.join(REQUIREMENTS_FOLDER, "requirements.txt"), 'r')]
test_requirements = [line.strip() for line in open(os.path.join(REQUIREMENTS_FOLDER, "requirements_dev.txt"), 'r')]


setup(
    name='diia_auth_server',
    version='{version}'.format(version=__version__),
    description="Web server for comunicationg with ID gov ua",
    long_description=get_long_description(),
    author="KyivTechSummit",
    author_email='anton.dasyuk@gmail.com',
    url='example.com/api/v1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "diia_auth_server": [
            "docs/*",
            "templates/*",
            "static/*",
            "static/js/*",
            "static/css/*",
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords="diia_auth_server",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'run_diia_auth_server=diia_auth_server.app:run_app',
            'init_example=diia_auth_server.init_example:init_example'
        ]
    }
)
