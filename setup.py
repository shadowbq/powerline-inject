
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

INSTALL_REQUIRES = [
    'kubernetes-py>=1.10.7.4',
    'powerline-status>=2.7',
    ]

def version():
    with open(os.path.abspath(__file__).replace('setup.py', 'version.meta'), 'r') as v:
        return v.read().replace('\n', '')

# Heavily inspired by the powerline-kubernetes library written by Vincent De Smet
# (vincent.drl@gmail.com) and located at https://github.com/so0k/powerline-kubernetes
setup(
    name='powerkube-fork',
    version=version(),
    description='A powerline segment to show kubernetes context items, with toggling and alert color functionality',
    author='Scott MacGregor',
    author_email='shadowbq@gmail.com',
    url='https://github.com/d2iq-shadowbq/powerkube-fork',
    download_url='https://github.com/d2iq-shadowbq/powerkube-fork/tarball/'+ version(),
    packages=['powerkube_fork'],
    python_requires='>=3.6',
    install_requires=INSTALL_REQUIRES,
    license='Copyright',
    keywords=['kubernetes_py','k8s','powerline','powerkube'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Terminals'
    ]
)
