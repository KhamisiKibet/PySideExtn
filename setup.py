import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PySideExtn", # Replace with your own username
    version="2.0.2",
    author="ANJAL.P. Improved by Khamisi Kibet",
    author_email="spinncompany@gmail.com",
    description="PySideExtn is an open-source Python programming language extension designed to empower PySide2, PyQt5, PySide6 or PyQt6 users with an expanded toolkit. This extension enriches the PySide2, PyQt5, PySide6 or PyQt6 library by introducing a range of additional widgets and features, significantly enhancing its capabilities and versatility.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KhamisiKibet/PySideExtn",
    keywords = ['PySide', 'PyQt', 'animation', 'custom', 'widgets', "QML", "C++", "QT Creator", "Moder GUI", "Desktop GUI", "Design"],   # Keywords that define your package best
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["qtpy"],
)