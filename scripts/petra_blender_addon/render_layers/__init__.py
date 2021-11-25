import importlib
import queue
import sys

import bpy


render_queue = queue.Queue()


def preview(identifier):
    print(f"[PETRA] Preview Layer: {identifier}")
    run_module("initialisation")
    run_module(identifier)


def render(identifier):
    render_queue.put(identifier)
    if render_queue.unfinished_tasks == 1:
        bpy.app.handlers.render_complete.append(render_complete)
        bpy.app.handlers.render_cancel.append(render_cancel)
        render_next()


# Helper methods


def render_next():

    if not render_queue.unfinished_tasks:
        print("[PETRA] Render completed.")
        bpy.app.handlers.render_complete.remove(render_complete)
        bpy.app.handlers.render_cancel.remove(render_cancel)
        return

    identifier = render_queue.get()

    print(f"[PETRA] Render Layer: {identifier}")

    run_module("initialisation")
    run_module(identifier)
    run_module("layer_render")


def render_complete(scene):
    task_done()


def render_cancel(scene):
    print("[PETRA] Render canceled.")
    task_done()


def task_done():
    render_queue.task_done()

    def in_3_seconds():
        render_next()

    bpy.app.timers.register(in_3_seconds, first_interval=3)


def run_module(identifier):
    module_name = f"{__name__}.{identifier}"
    if module_name not in sys.modules:
        importlib.import_module("." + identifier, __name__)
    else:
        importlib.reload(sys.modules[module_name])
