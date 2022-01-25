from setuptools import setup, find_packages

setup(
    name="Final-project",
    version="1.0",
    author="drg-v",
    author_email="gryban.v.2001@gmail.com",
    url="https://github.com/drg-v/final_project",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["Flask", "Flask-Cors", "Flask-Migrate", "flask-restful",
                      "Flask-SQLAlchemy", "numpy", "pandas", "PyJWT", "PyMySQL",
                      "pytest", "python-dotenv", "scikit-learn", "scipy", "Werkzeug",
                      "gunicorn", "pylint", "python-coveralls"]
)
