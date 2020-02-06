import docker

def docker_start(image, volumes={}, env_variables={}):
    """Start a long waiting idle program in container

    Return the container object to be used for 'docker exec' commands.
    """
    # Make sure to use the latest public version of the docker image
    client = docker.from_env()

    dvolumes = {host: {'bind': ctr, 'mode': 'rw'}
                for (ctr, host) in volumes.items()}

    print("Starting container with image %r", image)
    con = client.containers.run(image, ['sleep', '10000'], detach=True,
                                volumes=dvolumes, environment=env_variables)
    print("Started container %s", con.id[:12])
    return con

docker_start('quay.io/pypa/manylinux2014_s390x:latest')
