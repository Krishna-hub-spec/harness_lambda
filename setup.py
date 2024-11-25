from setuptools import setup, find_packages

setup(
    name="harness_project",  # Replace with your project name
    version="0.1.0",
    description="A simple Python project for CI/CD pipeline",
    author="Your Name",  # Replace with your name
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=[
        "flask>=2.3.3",  # Add your required dependencies
    ],
    python_requires=">=3.6",
)
