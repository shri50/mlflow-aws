# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from setuptools import setup, find_packages

setup(name='sagemaker-example',
      version='1.0',
      description='SageMaker MLFlow Example.',
      packages=find_packages(exclude=('tests', 'docs')))
