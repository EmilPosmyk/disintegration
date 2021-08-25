from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='disintegration',
      version="0.0.3",
      author='Disintegrated persona n.g.',
      description="Reintegrating disintegrated ",
      packages=find_packages(),
      #packages=setuptools.find_packages(where="disintegration"),
      install_requires=requirements,
      test_suite='tests',
      # url="https://github.com/Alien/disintegration",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/disintegration-run'],
      zip_safe=False,
      py_modules=['disintegration'],
      entry_points='''
              [console_scripts]
              disintegration=disintegration:main
          ''',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
      ],
      # package_dir={"": "disintegration"},
      python_requires=">=3.8",
)
