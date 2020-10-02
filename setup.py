import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twitch-notifications", # Replace with your own username
    version="0.1",
    author="Fam0r",
    description="Twitch chat notifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fam0r/twitch-notifications",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
        "Topic :: Communications :: Chat :: Internet Relay Chat"
    ]
)