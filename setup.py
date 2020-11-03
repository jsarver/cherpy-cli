from distutils.core import setup

from setuptools import find_packages

setup(
    name='cherpy_tools',
    version='0.5.2',
    packages=find_packages(),
    url='',
    license='',
    author='Josh Sarver',
    author_email='josh.sarver@gmail.com',
    description='Cherwell Admin Toolkit',
    install_requires=["""cherpy
                        loguru
                        colorama>=0.3.4
                        zeep
                        pyyaml
                        requests
                        click
    """, 'click'],
    entry_points="""
    [console_scripts]
    search=cherpy_tools.cli_tools:search_object_cli
    delete_objects=cherpy_tools.cli_tools:delete_objects_cli
    update=cherpy_tools.cli_tools:update_object_cli
    create=cherpy_tools.cli_tools:create_object
    run-onestep=cherpy_tools.cli_tools:run_onestep_cli
    csm=cherpy_tools.cli_tools:csm
    """

)
