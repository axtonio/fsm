from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    more_description = f.read()


setup(
    name="fsm",
    version="2.2.6",
    author="Antonio Rodrigues",
    author_email="axtonio.code@gmail.com",
    description="Library for working with finite state machines",
    long_description=more_description,
    long_description_content_type="text/markdown",
    url="https://github.com/axtonio/fsm",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
        "python-frontmatter",
        "terminal_app @ git+https://github.com/axtonio/terminal_app.git@v1.0.3",
        "markdown_reader @ git+https://github.com/axtonio/markdown_reader.git@v2.0.0",
    ],
)
