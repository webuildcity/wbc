#!/bin/bash
coverage run runtests.py
coverage html --include=../wbc/*
