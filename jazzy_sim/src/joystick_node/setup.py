from setuptools import find_packages, setup

import os
from glob import glob 

package_name = 'joystick_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ((os.path.join('share', package_name), glob('launch/*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Anuj Patel',
    maintainer_email='anuj@neuralzome.com',
    description='Joystick Node to Control Edubot',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joystick_node = joystick_node.joystick_node:main',
        ],
    },
)