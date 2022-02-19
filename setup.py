import setuptools
import pathlib

with open(pathlib.Path(__file__).parent / "README.md", "r") as readme:
	readme_text = readme.read()

setuptools.setup(
	name="pyconversation",
	version="1.0.0",
	author="Roman Melamud",
	description="Zero-dependency library for chat-bot creators with deadlines. It allows you to describe a conversation, talk with user according to your schema and restore it, if something went wrong.",
	long_description=readme_text,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
	],
	python_requires=">=3.6",
	py_modules=["pyconversation"],
	package_dir={"": "pyconversation/src"},
	install_requires=[],
)
