from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'pub_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),   # <-- ADD THIS
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sahana',
    maintainer_email='arulsahana2005@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "number_publisher = pub_sub.number_publisher:main",
            "number_subscriber = pub_sub.number_subscriber:main"
        ],
    },
)
