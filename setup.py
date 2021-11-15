import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tool_zap",
    version="0.0.1",
    description="Collection of command line string processing tools that can be used locally or remotely",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SirGnip/tool_zap",

    # Code is in "src/", an un-importable directory (at least not easily or accidentally)
    # Helps reduce confusion around whether code from repo or site-packages is being used.
    # https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
    # https://hynek.me/articles/testing-packaging/
    # https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6',
    install_requires=[
        # 3rd party dependencies
        "pytest==5.3.1",
        "pytest-cov==2.8.1",
        "pylint==2.4.4",
    ],
    entry_points={
        "console_scripts": [
            "tzblock_exp = tool_zap.tools.cli.tzblock_exp:cli",
            "tzcounts = tool_zap.tools.cli.tzcounts:cli",
            "tzgrepline = tool_zap.tools.cli.tzgrepline:cli",
            "tzjoin = tool_zap.tools.cli.tzjoin:cli",
            "tzline_exp = tool_zap.tools.cli.tzline_exp:cli",
            "tzlines_exp = tool_zap.tools.cli.tzlines_exp:cli",
            "tzsplit = tool_zap.tools.cli.tzsplit:cli",
        ]
    },
)
