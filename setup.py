from setuptools import setup, find_packages


def get_requirements(file_path:str)->list[str]:
#    return list of requirements from requirements.txt file
    requirements =[]
    with open(file_path,'r') as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements ]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

    



setup(
    name='pytorch-rl',
    version='0.0.1',
    description='End to End ML Project',
    author='Aditya Ghai',
    author_email='adityaghailbdrp1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')





)