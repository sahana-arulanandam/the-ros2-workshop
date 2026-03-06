import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'two_wheel'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Include all launch files
	(os.path.join('share', package_name, 'launch'), glob('launch/*.py') + glob('launch/*.launch')),
        # Include all URDF files
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        # Include all mesh files (STL)
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
        # Include RViz configs
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
        # Include Worlds
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akash',
    maintainer_email='akashsaiambati@gmail.com',
    description='Two wheel differential drive robot package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_controller = two_wheel.robot_controller:main',
        ],
    },
)
