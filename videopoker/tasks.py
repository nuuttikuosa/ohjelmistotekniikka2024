from invoke import task
from sys import platform
import subprocess

@task
def start(ctx):
   ctx.run("python3 src/index.py", pty=True)

@task
def startGUI(ctx):
   ctx.run("python3 src/index2.py", pty=True)



@task
def coverage(ctx):
   ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
   ctx.run("coverage html", pty=True)
   if platform != "win32":
      subprocess.Popen(["xdg-open", "htmlcov/index.html"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def format(ctx):
   ctx.run("autopep8 --in-place --recursive src", pty=True)

@task(format)
def lint(ctx):
   ctx.run("pylint src", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)

