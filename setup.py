try:
    from setuptools import setup
    
    
except ImportError:
    from distutils.core import setup

config = {
            'description':'Transport and Cargo logistics Management Suite', 
            'author': 'Chibuzor Ogbu',
            'url': 'http://www.byteworksng.com',
            'download_url': 'http://www.byteworksng.com/downloads/tackle',
            'author_email': 'chibuzorogbu@gmail.com',
            'version': '0.Alpha.1',
            'install_requires': ['nose'],
            'packages': ['tackle', 'kivy'],
            'scripts': [],
            'name': 'Tackle'
}

setup(**config)
        
    
