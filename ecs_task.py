import json
import subprocess
import tempfile
import boto3

ecs = boto3.client('ecs',region_name='us-east-2')
"""Client interface for ECS"""
def register_ecs(family, task_role_arn, ecs_task_definition):
    """Register an ECS task definition and return it.

    Positional parameters:
                 family -- the name of the task family
          task_role_arn -- the ARN of the task's role
    ecs_task_definition -- the task definition, as returned by Micah
                           Hausler's script
    """
    ecs_task_definition['family'] = family
    ecs_task_definition['taskRoleArn'] = task_role_arn
    return ecs.register_task_definition(
        family=family,
        taskRoleArn=task_role_arn,
        containerDefinitions=ecs_task_definition['containerDefinitions'],
    )

def create_cluster(name):
    """Create an ECS cluster, return it.

    Positional parameters:
    name -- Name for the cluster, must be unique.
    """
    return ecs.create_cluster(
        clusterName=name,
    )

def ecs_from_dc(dc_path):
    """Reads a docker-compose file to return an ECS task definition.

    Positional arguments:
    dc_path -- Path to the docker-compose file.
    """
    with open(dc_path, 'r') as dc_file, tempfile.TemporaryFile('w+t') as tmp:
        subprocess.check_call(
            [
                '/usr/bin/env',
                'docker',
                'run',
                '--rm',
                '-i',
                'micahhausler/container-transform'
            ],
            stdin=dc_file,
            stdout=tmp,
        )
        tmp.seek(0)
        ecs_task_definition = json.load(tmp)
        return ecs_task_definition

print register_ecs('hitcounter-redis', '*', ecs_from_dc("./docker-compose.yml"))
print create_cluster('hitcounter-redis')
