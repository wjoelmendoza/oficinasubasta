from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.distutils")

name = "OficinaSubasta"
default_task = ["publish", "analyze"]
version="0.1.dev0"


@init
def set_properties(project):
    project.depends_on("flask")
    project.depends_on("flask_restful")

    project.set_property("flake8_verbose_output", True)
    project.set_property("flake8_include_scripts", True)
