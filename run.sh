#!/bin/bash
uv run gunicorn --workers 4 --bind :5000 "main:flapp"
