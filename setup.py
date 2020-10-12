import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TwitchNotifications",
    version="0.5",
    author="Fam0r",
    author_email="fam0riizi@gmail.com",
    description="Twitch chat notifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fam0r/TwitchNotifications",
    packages=['TwitchNotifications'],
    entry_points={
        'console_scripts': [
            'TwitchNotifications=TwitchNotifications:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
        "Topic :: Communications :: Chat :: Internet Relay Chat"
    ]
)