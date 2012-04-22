# Copyright header

from syn.system import cd, run, mkdir, putenv, abspath
from syn.db import Database
import os

def preform_step(step_name):
    return run(["synd/build", step_name])


def compose_source_archive(unpacked_root, upstream_tarball):
    """
    Generate a signing Database, correctly named tarball and
    a syn local tarball.
    """
    pass


def extract_source_archive(signed_database, root):
    """
    Verify the SHA sums, and compose a correctly formed
    unpacked syn source directory using the archives noted
    in the signed db
    """
    pass


def build_source_package(root, steps):
    with cd(root):
        metainf = Database("synd/metainf")
        mkdir("synd/tmp", destroy_old=True)
        putenv("SYN_DESTDIR", abspath("synd/tmp"))
        for step in steps:
            preform_step(step)
        # We've now got our tree (magically) in synd/tmp
        # Let's package it nicely.
