# coding=utf-8

from invoke import task


@task
def pep8(ctx):
  ctx.run("pep8 {{cookiecutter.project_slug}} {{cookiecutter.project_slug}}_test")


@task
def lint(ctx):
  ctx.run("pylint {{cookiecutter.project_slug}} {{cookiecutter.project_slug}}_test -r n")


@task
def test(ctx):
  ctx.run("py.test -v --cov {{cookiecutter.project_slug}} --cov-report=html --cov-report=term-missing {{cookiecutter.project_slug}}_test")


@task(pre=[test, pep8, lint])
def check(ctx):
  pass




