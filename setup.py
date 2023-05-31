import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

version = "0.0.0"

REPO_NAME="Text-summerizer-project"
AUTHOR_USER_NAME="suprio99"
SRC_REPO="textSummerizer"
AUTHOR_EMAIL="samantasuprio88@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/" + AUTHOR_USER_NAME + "/" + SRC_REPO + "/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(),
)