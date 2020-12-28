from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='concurrent-tool',
    version='0.0.1',
    packages=['concurrent-tool'],
    author="lvyunze",
    author_email="17817462542@163.com",
    description="Concurrent libraries for easy use of thread pools, process pools, and coroutines",
    keywords="thread pool、process pool、coroutines pool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lvyunze/concurrent-tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)