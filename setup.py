from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()
    
    setup(
        name="Crop_Recommendation_Model",
        version="1.0.0",
        description="Crop recommendation model using machine learning algorithms",
        author="Digraskar Pratik",
        author_email= "digraskarpratik1@gmail.com")
    