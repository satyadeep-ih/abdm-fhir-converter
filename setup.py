from setuptools import find_packages, setup

setup(
    name='abdm_fhir_converter',
    packages=find_packages(include=['fhir_converter']),
    version='0.0.5',
    description='Intelehealth fhir converter',
    install_requires=["fhir.resources"],
    author='Satyadeep',
)
