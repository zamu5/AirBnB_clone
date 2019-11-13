#!/usr/bin/python3
"""link storage to modules"""


from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
