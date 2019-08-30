from django.test import TestCase
from django.views.generic.base import View
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from json import dumps
import datetime
from random import randint
from re import match as match
from .models import UserInfo
from .models import UnauthorizedUserInfo
from Project.models import UserProjectAuthority
from .get_info_dict import *
from .utils import FileHelper,is_pc,make_sense
import os
from os.path import exists,join
# Create your tests here.

test = make_password("Admin12345", "OmniSci", 'pbkdf2_sha256')
print(test)