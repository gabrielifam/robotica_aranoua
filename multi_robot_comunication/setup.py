from setuptools import setup
import os
from glob import glob

package_name = 'multi_robot_comunication'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'msg'), glob('msg/*.msg')),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Multi-robot comunication package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_1 = multi_robot_comunication.robot_1:main',
            'robot_2 = multi_robot_comunication.robot_2:main',
            'robot_3 = multi_robot_comunication.robot_3:main',
        ],
    },
)