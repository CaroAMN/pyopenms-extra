import setuptools


setuptools.setup(
    name="ProteomicLFQ Application", 
    version="1.0.0",
    author="Carolin Schwitalla, Hristian Gabrovski, Alexander Gebhard",
    description="not yet done",
    url="https://github.com/CaroAMN/Teamprojekt/tree/Mainapp_Caro",
    packages=setuptools.find_packages(),
    package_data={'Pictures' : ['src/Pictures/OpenMS2.png']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)