from setuptools import find_packages, setup

package_name = 'dofbotx_config'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Felipe Rivas',
    maintainer_email='rivascf@gmail.com',
    description='DofbotX configuration package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'param_srv = dofbotx_config.parameter_server:init_srv'
        ],
    },
)
