# coding=utf-8

from invoke import task

@task
def lint(ctx):
  ctx.run("pylint {{cookiecutter.project_slug}} {{cookiecutter.project_slug}}_test")


@task
def test(ctx):
  ctx.run("py.test --cov {{cookiecutter.project_slug}}")


@task(pre=[test, lint])
def check(ctx):
  pass




