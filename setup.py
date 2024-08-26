from setuptools import setup, find_packages

setup(
    name="chatgpt_orm",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "annotated-types==0.7.0",
        "anyio==4.4.0",
        "certifi==2024.7.4",
        "colorama==0.4.6",
        "distro==1.9.0",
        "h11==0.14.0",
        "httpcore==1.0.5",
        "httpx==0.27.0",
        "idna==3.8",
        "jiter==0.5.0",
        "openai==1.42.0",
        "pydantic==2.8.2",
        "pydantic_core==2.20.1",
        "sniffio==1.3.1",
        "tqdm==4.66.5",
        "typing_extensions==4.12.2",
    ],
    test_suite="tests",
)
