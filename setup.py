from setuptools import setup, find_packages

setup(
    name="pinch-analysis",
    version="0.1.0",
    description="Pinch-point technique for heat integration analysis in chemical plants.",
    url="https://github.com/ahoetker/pinch-analysis",
    author="Andrew Hoetker, Emma Holle, James Taylor, Steve Wilson",
    author_email="ahoetker@me.com",
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        pinch-analysis=pinch.scripts.cli:cli
    """,
    packages=find_packages(),
    zip_safe=False,
)