from setuptools import setup,find_packages

def get_requires(file_path):
    with open(file_path, 'r') as f:
        requires=f.readlines()
        requires=[req.replace('\n','') for req in requires]
        if '-e .' in requires:
            requires.remove('-e .')
    return requires

setup(
    name='Smart_Research_Assistant_Using_Autogen',
    version='1.0.0',
    description='An End to End Smart Research Agent that helps you in finding & summarization of research articles ',
    author='aky-ds',
    author_email='www.ayazkhan.com.21@example.com',
    url='https://github.com/your_username/my_package',
    packages=find_packages(),
    install_requires= get_requires('requirements.txt'),
)