#!/usr/bin/env bash

# Make sure dest dir exist
mkdir -p plot

# Create the graphics
gnuplot plot.gpi
