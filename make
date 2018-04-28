#!/bin/bash

pandoc slides.md -H latex/header.tex -t beamer -o slides.pdf
