def hex_to_rgb(value):
    return tuple(int(value.lstrip('#')[i:i+2], 16) / 255 for i in (0, 2, 4))

def glasbey_cmap():
    from colorcet import glasbey
    from matplotlib.colors import LinearSegmentedColormap
    # Convert hexadecimals to list of rgb tuples
    glasbey_rgb = [hex_to_rgb(color) for color in glasbey]
    # Make first color black for background
    glasbey_rgb[0] = (0.,0.,0.)
    # Create colormap object for matplotlib
    glasbey_cm = LinearSegmentedColormap.from_list('glasbey', glasbey_rgb)
    return glasbey_cm