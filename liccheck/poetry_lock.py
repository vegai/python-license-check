import pkg_resources
import toml


def parse_poetry_lock(poetry_lock_file):
    requirements = []
    poetry_lock = toml.loads(open(poetry_lock_file).read())
    for key in poetry_lock["package"]:
        pkg_name = f'{key["name"]}=={key["version"]}'
        requirements.append(pkg_resources.Requirement.parse(pkg_name))

    return requirements


def resolve_without_deps(requirements):
    working_set = pkg_resources.working_set
    for req in requirements:
        env = pkg_resources.Environment(working_set.entries)
        dist = env.best_match(
            req=req, working_set=working_set, installer=None, replace_conflicting=False,
        )
        yield dist


def resolve(requirements):
    for dist in pkg_resources.working_set.resolve(requirements):
        yield dist
