# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from pathlib_mate import Path
from diskcache import Cache


HOME = Path.home()
ALFRED_DIR = Path(HOME, ".alfred-english-learner")
if not ALFRED_DIR.exists():
    ALFRED_DIR.mkdir()

CACHE_DIR = Path(ALFRED_DIR, ".cache")

disk_cache = Cache(CACHE_DIR.abspath)
