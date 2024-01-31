from setuptools import setup, find_packages

setup(
    name='EmailAccountCreationApp',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Automated bulk email account creation application',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourgithub/EmailAccountCreationApp',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'email_creator=email_creator.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
)