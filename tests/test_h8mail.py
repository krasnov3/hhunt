#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `hhunt` package."""


import unittest
import sys
import time
import tempfile
import shutil
import contextlib
import os
import tarfile
import gzip
import argparse
from hhunt.utils import run
from hhunt.utils import classes
from hhunt.utils import helpers
from hhunt.utils import localsearch
from hhunt.utils import localgzipsearch

def print_test_banner(testname):
    print("========================")
    print("========================")
    print("\tTESTING: "+testname)
    print("========================")
    print("========================")


def make_temp_directory():
    emails = """
    krasnov@tutanota.de
    gandon@gmail.com
    fijsdhkfnhqsdkf
    fdqfqsdff
    hui@evilcorp.com
    notfound@email.com
    """
    creds = """
    pidor@gmail.com:ParolHuesosa
    bloblfd
    fjsdkf,ds
    aaaaaa@deathsquad.com:An0therSECRETpassw0rd
    ddqsdqs
    """
    temp_dir = tempfile.mkdtemp()
    try:
        fd_emails = open(os.path.join(temp_dir, "test-emails.txt"), "w")
        fd_emails.writelines(emails)
        fd_emails.close()
        fd_creds = open(os.path.join(temp_dir, "test-creds.txt"), "w")
        fd_creds.writelines(creds)
        fd_creds.close()
        tar = tarfile.open(os.path.join(temp_dir, "test-creds.tar.gz"), "w:gz")
        tar.add(os.path.join(temp_dir, "test-creds.txt"))
        tar.close()

        return temp_dir
    except Exception as e:
        print(e)


class Testhhunt(unittest.TestCase):
    """Tests for `hhunt` package."""

    def setUp(self):
        """Generating local files"""
        self.temp_dir = make_temp_directory()
        print("Created Temp Dir: " + self.temp_dir)
        print(os.listdir(self.temp_dir))
        self.filetargets = os.path.join(self.temp_dir, "test-emails.txt")
        self.filetxt = os.path.join(self.temp_dir, "test-creds.txt")
        self.filegz = os.path.join(self.temp_dir, "test-creds.tar.gz")
        print("Test files generated in : " + self.temp_dir)

        # a = open(self.filetxt, "r")
        # print(a.readlines())

    def tearDown(self):
        """Cleaning temp files"""
        print("Removing dir + content: " + self.temp_dir)
        shutil.rmtree(self.temp_dir)

    def test_000_simple(self):
        """Simple test"""
        run.print_banner()
        print_test_banner("VANILLA")

        user_args = run.parse_args(["-t", "test@example.com"])
        run.hhunt(user_args)

    def test_002_local_files_txt_gz(self):
        """Local file search Test"""
        run.print_banner()
        print_test_banner("TXT LOCAL")
        user_args_lb = run.parse_args(["-t", self.filetargets, "-lb", self.filetxt, "-sk"])
        run.hhunt(user_args_lb)
        print_test_banner("TXT LOCAL-SINGLFILE")
        user_args_lb = run.parse_args(["-t", self.filetargets, "-lb", self.filetxt, "-sk", "-sf"])
        run.hhunt(user_args_lb)

        run.print_banner()
        print_test_banner("GZ LOCAL")
        user_args_gz = run.parse_args(["-t", self.filetargets, "-gz", self.filegz, "-sk"])
        run.hhunt(user_args_gz)
        print_test_banner("GZ LOCAL-SINGLEFILE")
        user_args_gz = run.parse_args(["-t", self.filetargets, "-gz", self.filegz, "-sk", "-sf"])
        run.hhunt(user_args_gz)

    def test_003_url(self):
        run.print_banner()
        print_test_banner("URL-RAW")
        user_args_lb = run.parse_args(["-u", "https://raw.githubusercontent.com/khast3x/hhunt/master/tests/test_email.txt"])
        run.hhunt(user_args_lb)
        run.print_banner()
        print_test_banner("URL-MESSY")
        user_args_lb = run.parse_args(["-u", "https://raw.githubusercontent.com/khast3x/hhunt/master/tests/test_email.txt"])
        run.hhunt(user_args_lb)
