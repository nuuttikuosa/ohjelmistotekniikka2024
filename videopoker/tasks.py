from invoke import task
import subprocess
from sys import platform

@task
def foo(ctx):
   print("bar")

@task
def start(ctx):
   ctx.run("python3 src/index.py", pty=True)

@task
def coverage(ctx):
   ctx.run("coverage run --branch -m pytest src/", pty=True)

@task(coverage)
def coverage_report(ctx):
   ctx.run("coverage html", pty=True)
   if platform != "win32":
      subprocess.Popen(["xdg-open", "htmlcov/index.html"])
