from setuptools import find_packages, setup

package_name = 'nodos_topicos_py'

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
    maintainer='robousr',
    maintainer_email='erik.pena@ingenieria.unam.edu',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "primer_nodo = nodos_topicos_py.primer_nodo:main",
            "nodo_pub_numero =nodos_topicos_py.nodo_pub_numero:main",
            "nodo_contador =nodos_topicos_py.nodo_contador:main"
        ],
    },
)
