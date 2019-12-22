#!/bin/sh
gunicorn app.app:create_app --bind :8000 --worker-class aiohttp.worker.GunicornUVLoopWebWorker
