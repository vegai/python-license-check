import pkg_resources
import toml


def parse_poetry_lock(poetry_lock_file):
    requirements = []
    poetry_lock = toml.loads(open(poetry_lock_file).read())
    for key in poetry_lock["package"]:
        pkg_name = f'{key["name"]}=={key["version"]}'
        requirements.append(pkg_resources.Requirement.parse(pkg_name))

    return requirements
