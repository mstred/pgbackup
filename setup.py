from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()
    f.close()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Edson Samuel Jr',
    author_email='samuedson@gmail.com',
    description="A toy project from A Cloud Guru's Introduction to Python Development course",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mstred/pgbackup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main'
        ]
    }
)
