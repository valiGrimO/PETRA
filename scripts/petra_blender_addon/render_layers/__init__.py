from collections import deque
import importlib
import sys

import bpy


render_queue = deque()


def preview(identifier):
    print(f"[PETRA] Preview Layer: {identifier}")
    run_module("initialisation")
    run_module(identifier)


def render(identifiers):
    reset_render_queue()

    render_queue.extend(identifiers)
    print(f"[PETRA] Render: queued {len(render_queue)} layers to render.")

    # add event listeners
    bpy.app.handlers.render_complete.append(when_one_layer_completed)
    bpy.app.handlers.render_cancel.append(when_one_layer_canceled)

    render_next()


# Events


def when_all_layers_completed():
    print("[PETRA] Render: all layers completed. ✅")
    bpy.app.handlers.render_complete.remove(when_one_layer_completed)
    bpy.app.handlers.render_cancel.remove(when_one_layer_canceled)


def when_one_layer_completed(scene):
    print("[PETRA] Render: one layer completed.")
    render_next_after_delay()


def when_one_layer_canceled(scene):
    print("[PETRA] Render: canceled. ❌")
    reset_render_queue()


# Helper methods


def render_next():
    if not render_queue:
        when_all_layers_completed()
        return

    identifier = render_queue.popleft()
    print(f"[PETRA] Render: {identifier}")

    try:
        run_module("initialisation")
        run_module(identifier)
        run_module("layer_render")
    except Exception as e:
        render_next_after_delay()
        raise e


def render_next_after_delay():
    # We add a 3 second delay here since running it right away
    # sometimes leads to issues. This might be revisited again
    # at a later point.

    def in_3_seconds():
        render_next()

    bpy.app.timers.register(in_3_seconds, first_interval=3)


def reset_render_queue():
    """
    Note: This function may be removed in the future. Adding it to
    ensure we start with a clean state amidst errors.
    """
    # remove unfinished tasks from previous unfinished render
    render_queue.clear()

    # remove potential event listeners from previous unfinished renders
    for func in bpy.app.handlers.render_complete:
        if func.__name__ == "when_one_layer_completed":
            bpy.app.handlers.render_complete.remove(func)

    for func in bpy.app.handlers.render_cancel:
        if func.__name__ == "when_one_layer_canceled":
            bpy.app.handlers.render_cancel.remove(func)


def run_module(identifier):
    module_name = f"{__name__}.{identifier}"
    if module_name not in sys.modules:
        importlib.import_module("." + identifier, __name__)
    else:
        importlib.reload(sys.modules[module_name])
