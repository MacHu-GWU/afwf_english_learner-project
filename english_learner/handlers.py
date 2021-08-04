# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import workflow
from .settings import disk_cache
from .google_complete import gc



def handler(wf, args=None):
    """
    :type wf: workflow.Workflow3
    :type args: list[str]
    """
    if args is None:
        args = wf.args

    n_args = len(args)

    if n_args == 0:
        wf.add_item(
            title="Type your word ...",
        )

    elif n_args >= 1:
        query = " ".join(args)

        if query not in disk_cache:
            suggestion_list = gc.get(query)
            disk_cache.set(query, "\n".join(suggestion_list), expire=7 * 24 * 3600)
        suggestion_list = disk_cache.get(query).split("\n")

        for suggestion in suggestion_list:
            wf.add_item(
                title=suggestion,
                subtitle="Search Google For %s" % suggestion,
                arg=suggestion,
                autocomplete=suggestion,
                valid=True,
            )

    return wf
