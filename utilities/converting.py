import io
import base64


def save_to_base64(object):
    """
    Convert the given object to a base64 encoded string.

    Parameters:
    object : string(path to file) or matplotlib.pyplot.Axes
        If `object` is a string, it represents a file path. The function reads the file,
        encodes it to base64, and returns the encoded string.
        If `object` is a matplotlib.pyplot.Axes object, the function saves the plot to a
        bytes buffer, encodes it to base64, and returns the encoded string.

    Returns:
    str or None
        Returns a string containing the base64 encoded representation of the object.
        Returns None if an error occurs during the conversion process.
    """
    try:
        if isinstance(object, str): 
            with open(object, "rb") as file:
                plot_base64 = base64.b64encode(file.read()).decode('utf-8')
        else:
            buf = io.BytesIO()
            object.savefig(buf, format='png')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return plot_base64
