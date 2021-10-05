"""
Tools to interact with Blender.
"""


def remove_link(socket_out, socket_in):
    """
    Remove link from socket_out to socket_in.

    Example
    -------
    >>> remove_link(nodeRL.outputs[0], nodeHub.inputs[3])
    """
    node_tree = socket_out.node.id_data
    for link in socket_out.links:
        if link.to_socket == socket_in:
            node_tree.links.remove(link)
